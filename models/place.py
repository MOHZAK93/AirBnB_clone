#!/usr/bin/python3
"""Place Model"""

import uuid
from datetime import datetime, date
from models.base_model import BaseModel
from models import storage


class Place(BaseModel):
    """Derived from BaseModel"""
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