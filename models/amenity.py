#!/usr/bin/python3
"""Amenity Model"""

import uuid
from datetime import datetime, date
from models.base_model import BaseModel
from models import storage


class Amenity(BaseModel):
    """Derived from BaseModel"""
    name = ""
