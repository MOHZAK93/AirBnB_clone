#!/usr/bin/python3
"""Review Model"""

import uuid
from datetime import datetime, date
from models.base_model import BaseModel
from models import storage


class State(BaseModel):
    """Derived from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
