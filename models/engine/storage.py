""" This module contains the storage class for the database"""
from contextlib import contextmanager
from dotenv.main import load_dotenv
from os import environ
from sqlalchemy import (
    create_engine,
    event,
    text,
)
from sqlalchemy.orm import (
    sessionmaker,
    scoped_session,
)
from sqlalchemy.pool import QueuePool
from typing import (
    Dict,
    Type,
    Union,
)
from models.base import Base
from models.book import Book
from models.user import User


load_dotenv()

@event.listens_for(Book, "after_insert")
def update_user_uploads(mapper, connection, target):
    """ Updates the user's uploads """
    statement = text(
        "UPDATE users SET uploads = uploads + 1 WHERE id = '{}'".format(
            target.user_id))
    connection.execute(statement)


class Storage:
    """ database storage class """

    __engine = None

    def __init__(self, **kwargs):
        """ initializes storage class """

        uname = environ["DB_PUBLIB_USER"]
        passwd = environ["DB_PUBLIB_PASSWORD"]
        dbname = environ["DB_PUBLIB_NAME"]
        dbhost = environ["DB_PUBLIB_HOST"]
        if environ["DB_PUBLIB_MODE"] == "test" or kwargs.get("test", False):
            dbname = environ["DB_PUBLIB_TEST_NAME"]
        """ Remove echo when done testing """
        self.__engine = create_engine(
            'mysql+mysqlconnector://{}:{}@{}/{}'.format(
                uname, passwd, dbhost, dbname),
            pool_pre_ping=True,
            poolclass=QueuePool,
            pool_size=10)
        self.session_factory = sessionmaker(bind=self.__engine,
                                            expire_on_commit=False)
        self.Session = scoped_session(self.session_factory)
        if environ["DB_PUBLIB_MODE"] == "test" or kwargs.get("test", False):
            Base.metadata.drop_all(self.__engine, checkfirst=True)

    def reload(self) -> None:
        """ Reloads the session and create tables """

        Base.metadata.create_all(self.__engine)

    @contextmanager
    def session_scope(self) -> None:
        """
            Creates a session, and tearsDown after control
            is transferred back
        """

        session = self.Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise Exception
        finally:
            session.close()

    def all(
        self,
        cls: Union[str, Type[User], Type[Book]] = None
    ) -> Dict[str, Union[User, Book]]:
        """ gets all objects or all of a specific class """

        objects = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            with self.session_scope() as session:
                query = session.query(cls)
                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        else:
            for model in [User, Book]:
                with self.session_scope() as session:
                    query = session.query(model)
                    for obj in query:
                        key = "{}.{}".format(obj.__class__.__name__, obj.id)
                        objects[key] = obj

        return objects

    def get(
            self,
            cls: Union[str, Type[User], Type[Book]],
            id: str) -> Union[User, Book]:
        """ gets a particular object """

        if type(cls) is str:
            cls = eval(cls)

        with self.session_scope() as session:
            try:
                obj = session.query(cls).filter(cls.id == id).one()
            except Exception:
                obj = None

        return obj

    def top(self, cls: Union[str, Type[User], Type[Book]], n: int) -> list:
        """ gets the top n users by uploads or books by downloads """
        if type(cls) is str:
            cls = eval(cls)

        with self.session_scope() as session:
            if cls == User:
                query = session.query(
                    User).order_by(User.uploads.desc()).limit(n).all()
            elif cls == Book:
                query = session.query(
                    Book).order_by(Book.downloads.desc()).limit(n).all()

        return query

    def lookup(self, email: str) -> Union[User, None]:
        """ Gets a user by email """

        with self.session_scope() as session:
            try:
                obj = session.query(User).filter(User.email == email).one()
            except Exception:
                obj = None
        return obj

    def count(self, cls: Union[str, Type[User], Type[Book]] = None) -> int:
        """ Returns the number of objects of a class """

        with self.session_scope() as session:
            if cls:
                if type(cls) is str:
                    cls = eval(cls)
                return session.query(cls).count()
            else:
                count = session.query(User).count()
                count += session.query(Book).count()
                return count

    def search(self, cls: Union[str, Type[User], Type[Book]], query: str) -> list:
        """ Searches for a book by title or author """

        if type(cls) is str:
            cls = eval(cls)

        with self.session_scope() as session:
            if cls == Book:
                query = session.query(
                    Book).filter(
                    Book.name.like(
                        '%{}%'.format(
                            query))).all()
            elif cls == User:
                query = session.query(
                    User).filter(
                    User.name.like(
                        '%{}%'.format(
                            query))).all()
        return query

    def add(self, obj: Union[User, Book], file=None) -> None:
        """ Adds an object to the current session """

        with self.session_scope() as session:
            session.add(obj)

    def save(self) -> None:
        """ Commits the current session - Used in lingering sessions """

        with self.session_scope() as session:
            session.commit()

    def delete(self, obj: Union[User, Book]) -> None:
        """ deletes an object from the current session """

        with self.session_scope() as session:
            session.delete(obj)

    def close(self) -> None:
        """ removes the current session """

        self.Session.remove()
