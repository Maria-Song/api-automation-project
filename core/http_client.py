import requests
import allure
from config import BASE_URL, TIMEOUT
from utils import get_logger

logger = get_logger(__name__)

class HttpClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()

    def send(self, method, url, **kwargs):
        url = self.base_url + url
        kwargs.setdefault("timeout", TIMEOUT)
        headers = kwargs.pop("headers", {})
        if hasattr(self, "headers"):
            headers.update(self.headers)
        kwargs["headers"] = headers

        # Allure 附件：请求概览
        allure.attach(f"{method} {url}", name="请求", attachment_type=allure.attachment_type.TEXT)
        if "json" in kwargs:
            allure.attach(str(kwargs["json"]), name="请求体", attachment_type=allure.attachment_type.TEXT)

        logger.info(f"请求：{method} {url}")
        resp = self.session.request(method, url, **kwargs)

        # Allure 附件：响应概览
        allure.attach(str(resp.status_code), name="状态码", attachment_type=allure.attachment_type.TEXT)
        allure.attach(resp.text[:1000], name="响应体(前1000字符)", attachment_type=allure.attachment_type.TEXT)

        logger.info(f"响应码：{resp.status_code}")
        return resp