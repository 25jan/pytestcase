# 题目：
# （1）计算机器（加法和除法）测试用例，使用fixture 实现setup/teardown 功能
# （2）使用第三方插件完成测试用例顺序的控制
# （3）编写的用例使用Allure工具生成测试（添加日志，截图）
import allure
import pytest


@allure.feature("计算器")
class Testcac:
    @pytest.mark.run(order=2)
    # @allure.story("加法")
    def test_add(self,getcalc):
        with allure.step("打开"):
            print("打开应用")
        with allure.step("相加"):
            result=getcalc.add(1,2)
        assert result == 3

    @pytest.mark.run(order=1)
    # @allure.story("除法")
    def test_div(self,getcalc):
        with allure.step("打开"):
            print("打开应用")
        with allure.step("相除"):
            result=getcalc.div(3,2)
        assert result == 1.5
