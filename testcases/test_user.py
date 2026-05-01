import pytest
import allure
from pathlib import Path
from utils import FileReader
from core import BaseApi, Assertions

data = FileReader.read_yaml(Path(__file__).parent.parent / "data" / "user_data.yaml")

@allure.feature("用户")
@allure.story("用户信息查询")
class TestUser:

    @pytest.mark.parametrize("case", data)
    @allure.title("{case[case_name]}")
    @allure.description("获取用户信息 GET 请求")
    def test_user(self, case):
        api = BaseApi()
        with allure.step(f"发送 {case['method']} 请求到 {case['url']}"):
            r = api.send(
                method=case["method"],
                url=case["url"],
                params=case.get("params"),
                json=case.get("json")
            )
        with allure.step("验证状态码"):
            Assertions.assert_code(r, case["expect_code"])