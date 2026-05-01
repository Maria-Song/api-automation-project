import pymysql
from dbutils.pooled_db import PooledDB
from config import DB_CONF
from utils.logger import get_logger

logger = get_logger(__name__)

class DBHelper:
    _pool = None
    @classmethod
    def init_pool(cls):
        if not cls._pool:
            cls._pool = PooledDB(creator=pymysql,** DB_CONF)  #初始化连接池
    @classmethod   #查询单条记录
    def query_one(cls, sql, args=None):
        cls.init_pool()
        conn = cls._pool.connection()
        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cur:
                cur.execute(sql, args or [])
                return cur.fetchone()
        finally:
            conn.close()