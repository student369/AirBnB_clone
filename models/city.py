#!/usr/bin/python3
"""City class which inherits from BaseModel."""

from models.base_model import BaseModel


class City(BaseModel):
    """City class to contain cities for app."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation."""
        super().__init__(self, *args, **kwargs)
