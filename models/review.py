#!/usr/bin/python3
"""Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review module"""

    place_id = ""
    user_id = ""
    text = ""
