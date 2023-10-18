#!/usr/bin/env python3

"""Create a Cache class"""
import redis
import uuid
from typing import Union
from typing import Callable

class Cache:
    """Cache class."""

    def __init__(self):
        """stores an instance of the Redis client as a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    def store(self, value):
        return self.redis_client.getset("key", value)

    def get(self, key, fn: Callable = None):
        value = self.redis_client.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key):
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key):
        return self.get(key, fn=int)
