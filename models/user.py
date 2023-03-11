#!/usr/bin/python3
"""User Model"""

import uuid
from datetime import datetime, date
from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """Derived from BaseModel"""
    email = ""

    password = ""

    first_name = ""

    last_name = ""
