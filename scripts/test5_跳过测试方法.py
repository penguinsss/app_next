import pytest


class Test5:
    @pytest.mark.skipif(True, reason='跳过方法') # 跳过
    def test_01(self):
        print('\n test01')

    @pytest.mark.skipif(False, reason='跳过方法')   # 不满足条件，不跳过
    def test_02(self):
        print('\n test02')

    @pytest.mark.skipif(reason='跳过方法')  # 跳过
    def test_03(self):
        print('\n test03')

    @pytest.mark.skipif()  # 跳过
    def test_04(self):
        print('\n test04')

    @pytest.mark.skipif(True)  # 报错
    def test_05(self):
        print('\n test05')

    @pytest.mark.skipif(True)  # 报错
    def test_06(self):
        print('\n test06')
