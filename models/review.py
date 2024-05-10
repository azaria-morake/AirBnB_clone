#!/usr/bin/python3
""" Review class """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Manages review objs """

    place_id = ""
    user_id = ""
    text = ""
