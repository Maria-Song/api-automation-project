# test_login.py
import pytest
import allure
from pathlib import Path
from utils.init import FileReader
from core.init import BaseApi, Assertions
from core.decorators import api_retry

data = FileReader.read_yaml(Path(__file__).parent.parent / "data" / "login_data.yaml")

@allure.feature("登录")          # 功能模块：一级分类
@allure.story("用户登录")        # 二级分类（可选）
class TestLogin:

    @pytest.mark.parametrize("case", data)
    @allure.title("{case[case_name]}")      # 动态标题：从 YAML 中取 case_name
    @allure.description("测试登录接口，验证状态码和返回内容")
    @api_retry()
    def test_login(self, case):
        api = BaseApi()
        with allure.step("发送登录请求"):          # 步骤1
            r = api.send(
                method=case["method"],
                url=case["url"],
                json=case.get("json")
            )
        with allure.step("断言状态码"):            # 步骤2
            Assertions.assert_code(r, case["expect_code"])
            # 如果 YAML 中有 expect_json 字段，则断言响应体
            if "expect_json" in case:
                Assertions.assert_json_equal(r, case["expect_json"])