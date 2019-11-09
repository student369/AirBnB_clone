#!/usr/bin/python3
"""Review Class which inherits from BaseModel class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review data for the app."""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Instantiation method."""
        super().__init__(self, *args, **kwargs)
