"""工厂函数之autouse"""
import pytest


@pytest.fixture(autouse=True)  # autouse=True时，login工厂函数不需要调用，会在每个测试方法执行前自动执行工厂函数
def login():
    print("\n 登录")


class Test_001:

    def test_001(self):
        print("\n test001")

    def test_002(self):
        print("\n test002")