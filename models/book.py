""" This module contains the Book class """
from sqlalchemy import (
    Table,
    DECIMAL,
    String,
    Column,
    Boolean,
    Integer,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from models.base import (
    BaseModel,
    Base,
)


class Book(BaseModel, Base):
    """ Book class """

    __tablename__ = "books"

    name = Column(
        String(255),
        nullable=False
    )

    public = Column(
        Boolean,
        default=True,
        nullable=False
    )

    author = Column(
        String(63),
        nullable=True
    )

    owner_id = Column(
        String(40),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=True
    )

    description = Column(
        String(1023),
        nullable=True
    )

    size = Column(
        Integer,
        nullable=True
    )

    downloads = Column(
        Integer,
        default=0,
        nullable=False
    )

    # Ref: Drive parameters
    parents = Column(
        String(40),
        nullable=True
    )

    driveId = Column(
        String(40),
        nullable=True
    )

    driveName = Column(
        String(255),
        nullable=True
    )

    downloadLink = Column(
        String(1023),
        nullable=True
    )

    thumbnailLink = Column(
        String(1023),
        nullable=True
    )

    iconLink = Column(
        String(1023),
        nullable=True
    )
