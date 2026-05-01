from core.http_client import HttpClient
from config.init import USER_CONF
from utils.logger import get_logger

logger = get_logger(__name__)

class BaseApi(HttpClient):
    token = ""
    def __init__(self): #构造函数 __init__
        super().__init__()
        self.headers = {"Content-Type": "application/json"}
        if BaseApi.token:
            self.headers["Authorization"] = f"Bearer {BaseApi.token}"
    def login_and_save_token(self):     #登录并保存 Token 的方法
        data = {"username": USER_CONF["username"], "password": USER_CONF["password"]}
        resp = self.send("POST", "/post", json=data)
        BaseApi.token = "test_token_123456"
        logger.info("登录成功，token已设置")