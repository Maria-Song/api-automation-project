import allure


class Assertions:
    @staticmethod
    def assert_code(resp, code):
        assert resp.status_code == code, f"期望状态码 {code}，实际 {resp.status_code}"

    @staticmethod
    def assert_json_equal(resp, expected):
        """校验响应 JSON 包含预期的键值对（支持嵌套）"""
        try:
            actual = resp.json()
        except ValueError:
            raise AssertionError("响应不是有效的 JSON 格式")

        def check(actual_dict, expected_dict, path=""):
            for key, expected_value in expected_dict.items():
                full_key = f"{path}.{key}" if path else key
                assert key in actual_dict, f"响应中缺少字段 {full_key}"
                actual_value = actual_dict[key]
                if isinstance(expected_value, dict):
                    # 如果期望值是字典，递归检查
                    assert isinstance(actual_value, dict), f"字段 {full_key} 期望是字典，实际是 {type(actual_value)}"
                    check(actual_value, expected_value, full_key)
                else:
                    assert actual_value == expected_value, f"字段 {full_key} 期望值 {expected_value}，实际值 {actual_value}"

        check(actual, expected)