import pytest
from appium import webdriver
from selenium.webdriver.common.by import By

from po练习.base import Base


def data():
    return [('1', '休眠'), ('m', 'MAC地址'), ('w', 'WPS按钮')]


class Test_ParamData:

    def setup_class(self):
        desired_caps = {'platformName': 'android',
                        'platformVersionName': '5.1',
                        'deviceName': 'sanxing',
                        'appPackage': 'com.android.settings',
                        'appActivity': '.Settings',
                        'unicodeKeyboard': True}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.base = Base(self.driver)
        self.search_btn = (By.ID, 'com.android.settings:id/search')
        self.search_text = (By.ID, 'android:id/search_src_text')
        self.search_result = (By.ID, 'com.android.settings:id/title')

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope='class', autouse=True)
    def go_to_search(self):
        self.base.click_ele(self.search_btn)

    @pytest.mark.parametrize('key, res', data())
    def test_001(self, key, res):
        self.base.send_ele(self.search_text, key)

        ele_list = self.base.search_eles(self.search_result)
        assert res in [i.text for i in ele_list]
