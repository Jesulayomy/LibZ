#!/usr/bin/python3
""" User class for all """
import enum

from datetime import datetime
from email_validator import validate_email
from flask_login import UserMixin
from hashlib import md5
from sqlalchemy import (
    String,
    Column,
    DateTime,
)
from sqlalchemy.orm import relationship
from typing import Any

from models.base import (
    BaseModel,
    Base,
)


class User(BaseModel, UserMixin, Base):
    """ User class """

    __tablename__ = "users"

    first_name = Column(
        String(63),
        nullable=False
    )

    last_name = Column(
        String(63),
        nullable=False
    )

    display_name = Column(
        String(63),
        nullable=True
    )

    gender = Column(
        String(7),
        default='male',
        nullable=False
    )

    date_of_birth = Column(
        DateTime,
        nullable=True
    )

    email = Column(
        String(255),
        nullable=False,
        unique=True
    )

    phone = Column(
        String(20),
        unique=True
    )

    password = Column(
        String(64),
        nullable=False
    )

    my_books = relationship(
        "Book",
        backref="owner",
        passive_deletes=True
    )

    # Drive folder refrencing user
    folder = Column(
        String(40),
        nullable=True
    )

    def __setattr__(self, name: str, value: Any) -> None:
        """ Sets attributes for the user class """

        if name == "first_name" or name == "last_name":
            if not value.isalpha():
                raise ValueError("Names must contain only letters")

        if name == "email":
            try:
                validate_email(value)
            except Exception:
                raise ValueError("Email address is invalid")

        # Info: Could we send the password encoded to avoid
        # sending sensitive data?
        if name == "password":
            md5_hash = md5()
            md5_hash.update(value.encode("utf-8"))
            value = md5_hash.hexdigest()

        if name == "date_of_birth":
            value = datetime.fromisoformat(value)

        super().__setattr__(name, value)
