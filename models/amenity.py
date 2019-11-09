#!/usr/bin/python3
"""Amenity class which inherits from BaseModel class."""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """All the amenities for the app."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of Amenity class."""
        super().__init__(self, *args, **kwargs)
