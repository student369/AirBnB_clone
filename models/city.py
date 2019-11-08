#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module city

This module contains the City class

"""
from models import base_model as b


class City(b.BaseModel):
    """City class

    A simple City class
    """
    state_id = ""
    name = ""
