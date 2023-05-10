#!/usr/bin/env python3
""" A module to cache the number of times a url
    was accessed
"""
import redis
import requests
from functools import wraps
from typing import Callable


Redis = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """ Caches the no of times a website was accessed """
    @wraps(method)
    def cache(url) -> str:
        """ Where the caching happens"""
        Redis.incr(f'count:{url}')
        result = Redis.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        Redis.set(f'count:{url}', 0)
        Redis.setex(f'result:{url}', 10, result)
        return result
    return cache


@data_cacher
def get_page(url: str) -> str:
    """ We cache the url before returning it's contents """
    return requests.get(url).text
