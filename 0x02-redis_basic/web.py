#!/usr/bin/env python3
""" Advanced - Module for Implementing an expiring
    web cache and tracker
"""
import requests
import redis
import time
from functools import wraps
from typing import Callable

redis_instance = redis.Redis()

def cache_result(expiration: int) -> Callable:
    """
    Decorator that caches the result of a method using Redis.

    Args:
        expiration: Expiration time for the cached result in seconds.

    Returns:
        Callable: Decorator function.
    """
    def decorator(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(url: str) -> str:
            """
            Wrapper function that tracks URL access count, caches the result, and returns it.

            Args:
                url: The URL to fetch the page content from.

            Returns:
                str: The HTML content of the URL.

            """
            key = f"count:{url}"
            count = redis_instance.get(key)
            if count is None:
                count = 0
            else:
                count = int(count)

            count += 1
            redis_instance.set(key, count, ex=expiration)

            result_key = f"result:{url}"
            result = redis_instance.get(result_key)
            if result is None:
                result = method(url)
                redis_instance.set(result_key, result, ex=expiration)

            return result
        return wrapper
    return decorator

@cache_result(expiration=10)
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL.

    Args:
        url: The URL to fetch the page content from.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text

url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.example.com"
print(get_page(url))
