import pytest
from core.base_api import BaseApi

@pytest.fixture(scope="session", autouse=True)
def login():
    api = BaseApi()
    api.login_and_save_token()
    yield