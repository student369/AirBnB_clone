#!/usr/bin/python3
"""User class which inherits from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """Users class."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """New user init method."""
        super().__init__(self, *args, **kwargs)
