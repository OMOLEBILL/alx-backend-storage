#!/usr/bin/env python3
""" We create a class to store strings """
import uuid
import redis
from typing import Union, Callable, Optional


class Cache():
    """ cache class for reddis """

    def __init__(self):
        """ We initaliaze the instances of the class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ We generate a random key to store the data """
        Id = str(uuid.uuid4())
        self._redis.set(Id, data)
        return Id

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """ we decode the value of the given key """
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return val

    def get_str(self, key: str) -> str:
        """ We return a str """
        val = self._redis.get(key)
        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ we return an int """
        val = self._redis.get(key)
        try:
            val = int(val.decode("utf-8"))
        except Exception:
            val = 0
        return val
