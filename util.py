from appium import webdriver


def get_driver():
    desired_caps = {'platformName': 'android',  # 测试平台
                    'platformVersionName': '5.1',  # 测试版本，不写自动会去获取手机版本
                    'deviceName': 'sanxing',  # 设备名字，可以随便去写，但是不能为空
                    'appPackage': 'com.android.mms',
                    'appActivity': '.ui.ConversationList',
                    'unicodeKeyboard': True}
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
