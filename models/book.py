#!/usr/bin/python3
""" Event class for handling events """
import enum

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
        nullable=False
    )

    # Ref: Drive parameters
    createdTime = Column(
        DateTime,
        nullable=True
    )

    modifiedTime = Column(
        DateTime,
        nullable=True
    )

    driveId = Column(
        String(40),
        nullable=True
    )

    originalName = Column(
        String(255),
        nullable=True
    )

    downloadLink = Column(
        String(1023),
        nullable=True
    )

    size = Column(
        Integer,
        nullable=True
    )

    thumbnail = Column(
        String(1023),
        nullable=True
    )

    iconLink = Column(
        String(1023),
        nullable=True
    )

    parents = Column(
        String(40),
        nullable=True
    )

    description = Column(
        String(1023),
        nullable=True
    )
