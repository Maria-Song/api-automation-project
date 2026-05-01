import pytest
import allure
from pathlib import Path
from utils import FileReader
from core import BaseApi, Assertions
from core.decorators import api_retry

data = FileReader.read_yaml(Path(__file__).parent.parent / "data" / "order_data.yaml")

@allure.feature("订单")
@allure.story("订单操作")
class TestOrder:

    @pytest.mark.parametrize("case", data)
    @allure.title("{case[case_name]}")
    @allure.description("订单相关接口测试")
    @api_retry()   # 如果订单创建需要重试，可保留
    def test_order(self, case):
        api = BaseApi()
        with allure.step(f"发送请求: {case['method']} {case['url']}"):
            r = api.send(
                method=case["method"],
                url=case["url"],
                params=case.get("params"),
                json=case.get("json")
            )
        with allure.step("检查状态码"):
            Assertions.assert_code(r, case["expect_code"])