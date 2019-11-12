#!/usr/bin/python3
"""A init configuration."""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
