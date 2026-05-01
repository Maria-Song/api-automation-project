import functools
import time
import requests
from config.settings import RETRY
from utils.logger import get_logger

logger = get_logger(__name__)

def api_retry(retry_times=None, delay=1):
    """
    重试装饰器，仅对网络相关异常重试
    :param retry_times: 重试次数，如果不传则使用配置中的 RETRY
    :param delay: 每次重试前的等待时间（秒）
    """
    if retry_times is None:
        retry_times = RETRY

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(retry_times + 1):
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, ConnectionError, TimeoutError) as e:
                    if i == retry_times:
                        logger.error(f"重试 {retry_times} 次后仍然失败")
                        raise
                    logger.warning(f"第 {i+1} 次重试，错误：{type(e).__name__} - {e}")
                    time.sleep(delay)
            # 正常情况下不会走到这里
            return None
        return wrapper
    return decorator