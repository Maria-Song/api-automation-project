import redis
from config import REDIS_CONF

class RedisHelper:    #获取 Redis 客户端（单例模式）
    _client = None
    @classmethod
    def get_client(cls):
        if not cls._client:
            cls._client = redis.Redis(**REDIS_CONF, decode_responses=True)
        return cls._client
    @classmethod    #设置缓存值（set）
    def set(cls, k, v, ex=None): return cls.get_client().set(k, v, ex=ex)
    @classmethod    #获取缓存值（get）
    def get(cls, k): return cls.get_client().get(k)