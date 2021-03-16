from flask import session
import os
import redis
import json
import uuid

redis_host = os.getenv('REDIS_SERVER', 'redis')
redis_port = os.getenv('REDIS_PORT', '6379')
redis_expire = os.getenv('REDIS_EXPIRE', '14400')
print(f"Using redis host at : {redis_host}:{redis_port}, with expire {redis_expire} seconds")

try:
    redisClient = redis.Redis(redis_host, port=redis_port, db=0, decode_responses=True) # short timeout for the test
    redisClient.ping() 
except:
    print(f"Redis is not running.")
    exit(0)

def getOrder():
    if not session.get('uuid'):
        session['uuid'] = uuid.uuid4().hex
    key = session.get('uuid')
    order = redisClient.get(key)
    if ((order == None) or ("uuid" not in order)):
        print(f"Order is None")
        order = {
            'uuid' : key
        }
        setOrder(order)
        return order
    else:
        # print(f"Order : {order}")
        j = json.loads(order)
        return j

def setOrder(order):
    key = session.get('uuid')
    res = redisClient.setex(key, redis_expire, json.dumps(order))

