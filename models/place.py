#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module place

This module contains the Place class

"""
from models import base_model as b


class Place(b.BaseModel):
    """Place class

    A simple Place class
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
