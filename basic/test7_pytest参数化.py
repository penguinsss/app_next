import pytest


class Test_ParamOne:

    @pytest.mark.parametrize('num', [1, 2, 3, 4])  # 上面申明，下面可以不使用 但不能不传递
    def test_001(self, num):  # 参数名必须要和申明的参数一致
        assert num != 2


def data():
    return [(1, 2, 3), (4, 4, 8)]


class Test_ParamMore:

    @pytest.mark.parametrize('a, b, c', data())
    def test_001(self, a, b, c):
        assert a + b == c
