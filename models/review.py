#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module review

This module contains the Review class

"""
from models import base_model as b


class Review(b.BaseModel):
    """Review class

    A simple Review class
    """
    place_id = ""
    user_id = ""
    text = ""
