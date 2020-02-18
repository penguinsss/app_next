import pytest

# 注意：类级别的工厂函数  如果在类内部，运行结果为整个类的setup_class之后优先运行；
#                       如果在类外部，运行结果为在整个类开始运行工厂函数
@pytest.fixture(scope='class', autouse=True)
def login():
    print("\n 登录")


class Test_003:

    @classmethod
    def setup_class(cls):
        print('\n setup_class')

    def test_001(self):
        print("\n 进入个人中心")

    def test_002(self):
        print("\n 查看订单")
