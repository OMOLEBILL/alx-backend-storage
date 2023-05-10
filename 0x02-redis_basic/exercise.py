#!/usr/bin/env python3
""" We create a class to store strings """
import uuid
import redis
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ We count the number of times a function is called """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ the increamental wrapper """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ we return the inputs and outputs of a callable """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ We wrap around a method to get input and out"""
        key = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", key)
        out = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", out)
        return out
    return wrapper


def replay(fn: Callable) -> None:
    """ We give history of calls to a function """
    Redis = redis.Redis()
    key = fn.__qualname__
    Calls = Redis.get(key)
    try:
        Calls = Calls.decode('utf-8')
    except Exception:
        Calls = 0
    print(f'{key} was called {Calls} times:')
    inputs = Redis.lrange(key + ":inputs", 0, -1)
    outputs = Redis.lrange(key + ":outputs", 0, -1)
    for x, y in zip(inputs, outputs):
        try:
            x = x.decode('utf-8')
        except Exception:
            x = ""
        try:
            y = y.decode('utf-8')
        except Exception:
            y = ""
        print(f'{key}(*{x}) -> {y}')


class Cache():
    """ cache class for reddis """

    def __init__(self):
        """ We initaliaze the instances of the class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
