import pytest


@pytest.fixture(params=[1, 2, 3, 4]) # 可以为元组，但不推荐
def data(request):  # 固定参数：request 等价于这个列表
    return request.param  # 固定写法，返回列表中的某个值


class Test_004:

    def test_004(self, data): # 只有参数引用才可以使用工厂函数的返回值
        assert data != 2
