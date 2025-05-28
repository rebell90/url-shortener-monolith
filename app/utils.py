import redis
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def get_cached_url(code: str):
    return r.get(code)

def set_cached_url(code: str, long_url: str, ttl_seconds=3600):
    r.set(code, long_url, ex=ttl_seconds)
