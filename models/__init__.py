#!/usr/bin/env python3
""" Initializes the storage """
from models.engine.storage import Storage
from models.engine.manager import Manager


storage = Storage()
storage.reload()

manager = Manager()
