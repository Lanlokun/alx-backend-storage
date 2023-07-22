#!/usr/bin/env python3
"""writing string to redis"""

import redis

from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    """Cache class"""
    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key, stores the input data in Redis using
        the random key and returns the key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    bytes,
                                                                    int,
                                                                    float]:
        """takes a key string argument and an optional Callable argument
        named fn. This callable will be used to convert the data back to
        desired format"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        """automatically parametrize Cache.get to str"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """automatically parametrize Cache.get to int"""
        return self.get(key, int)