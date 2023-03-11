#!/usr/bin/python3
"""City Model"""

import uuid
from datetime import datetime, date
from models.base_model import BaseModel
from models import storage


class City(BaseModel):
    """Derived from BaseModel"""

    state_id = ""
    name = ""
