from lib.designpattern import SingletonMeta
import redis

class RedisMachine(SingletonMeta):
    def __init__(self):
        self.pool = redis.Connection(host='localhost', port=6379, decode_responses=True, db= 2,password="momoca")
    
    def __getConnect(self):
        conn = redis.Redis(connection_pool=self.pool)
        return conn
    
    
    