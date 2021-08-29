
import pytest
import allure
from demo.calcdemo import Calc


@pytest.fixture(autouse=True,scope="class")
def getcalc():
    print("开始计算")
    calc =Calc()
    yield calc
    print("计算结束")
