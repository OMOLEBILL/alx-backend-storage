#!/usr/bin/env python3
""" We create a class to store strings """
import uuid
import redis
from typing import Union


class Cache():
    def __init__(self):
        """ We initaliaze the instances of the class """
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, float, int]) -> str:
        """ We generate a random key to store the data """
        Id = uuid.uuid4()
        self._redis.mset({str(Id): data})
        return str(Id)
