"""工厂函数之scope类级别"""
import pytest

# scope默认function，值可以是function class module session(慎用，每个session只运行一次)，
# 后两个用于编写插件使用，我们主要使用前两个
@pytest.fixture(scope='class', autouse=True)
def login():
    print("\n 登录")


class Test_002:

    def test_001(self):
        print("\n 进入个人中心")

    def test_002(self):
        print("\n 查看订单")