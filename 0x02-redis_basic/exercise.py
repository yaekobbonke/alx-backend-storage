#!/usr/bin/env python3

"""Create a Cache class"""
import redis
import uuid
from typing import Union

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
