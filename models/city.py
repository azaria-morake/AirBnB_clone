#!/usr/bin/python3
""" User class """

from models.base_model import BaseModel


class City(BaseModel):
    """ Manages city objs """

    state_id = ""
    name = ""
