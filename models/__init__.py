#!/usr/bin/python3
"""A init configuration to the file_storage."""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
