import pytest
from appium import webdriver


def get_driver():
    # 启动参数
    desired_caps = {'platformName': 'android',  # 测试平台
                    'platformVersionName': '5.1',  # 测试版本，不写自动会去获取手机版本
                    'deviceName': 'sanxing',  # 设备名字，可以随便去写，但是不能为空
                    'appPackage': 'com.android.settings',
                    'appActivity': '.Settings',
                    'unicodeKeyboard': True}
    # 接口地址：wd是webdriver的简写，hub代表一个中心节点
    # 声明手机驱动对象  结果：启动启动参数指定app，创建session，session相当于服务端的driver（脚本中叫driver），即一个session就是一个driver，一个session就是某一个app
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


def data():
    return [('1', '休眠'), ('m', 'MAC地址'), ('w', 'WPS按钮')]


class Test_ParamData:

    @classmethod
    def setup_class(cls):
        cls.driver = get_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.fixture(scope='class', autouse=True)
    def go_to_search(self):
        self.driver.find_element_by_id('com.android.settings:id/search').click()

    @pytest.mark.parametrize('key, res', data())
    def test_001(self, key, res):
        search_input = self.driver.find_element_by_id('android:id/search_src_text')
        search_input.clear()
        search_input.send_keys(key)
        ele_list = self.driver.find_elements_by_id('com.android.settings:id/title')
        assert res in [i.text for i in ele_list]
