import pytest


class Test6:
    # 标记预期失败，但还会执行一次测试方法
    @pytest.mark.xfail(True, reason='预期失败')    # xpassed
    def test_01(self):
        print('\n test01')
        assert True    # 断言通过，结果为xpass; 断言失败，结果为xfail，这种情况更合理

    @pytest.mark.xfail(True, reason='预期失败')   # xfailed
    def test_02(self):
        print('\n test02')
        assert False

    @pytest.mark.xfail(reason='预期失败')  # xfailed
    def test_03(self):
        print('\n test03')
        assert False

    @pytest.mark.xfail()     # xfailed
    def test_04(self):
        print('\n test04')
        assert False

    @pytest.mark.xfail(True)   # errors
    def test_05(self):
        print('\n test05')
        assert False

    @pytest.mark.xfail(False)  # errors
    def test_06(self):
        print('\n test06')
        assert False