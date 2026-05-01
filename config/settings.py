import os
import yaml
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
ENV_DIR = ROOT_DIR / "config" / "environments"
ENV = os.getenv("TEST_ENV", "test")

def load_env_config():
    config_path = ENV_DIR / f"{ENV}.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

CONFIG = load_env_config()

BASE_URL = CONFIG["base_url"]
TIMEOUT = CONFIG["timeout"]
RETRY = CONFIG["retry"]

DB_CONF = CONFIG.get("db", {})
REDIS_CONF = CONFIG.get("redis", {})
USER_CONF = CONFIG.get("user", {})

# ========== 用环境变量覆盖敏感字段 ==========
# 数据库密码
if os.getenv("DB_PASSWORD"):
    DB_CONF["password"] = os.getenv("DB_PASSWORD")

# Redis 密码
if os.getenv("REDIS_PASSWORD"):
    REDIS_CONF["password"] = os.getenv("REDIS_PASSWORD")

# 用户密码（如果测试环境需要动态覆盖）
if os.getenv("USER_PASSWORD"):
    USER_CONF["password"] = os.getenv("USER_PASSWORD")

# 可选：用户名也可以覆盖
if os.getenv("USER_USERNAME"):
    USER_CONF["username"] = os.getenv("USER_USERNAME")