from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def search_ele(self, loc, timeout=5, poll_frequency=1):
        """定位单个元素"""
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))  # 元组解包方式，和下标取值一样

    def search_eles(self, loc, timeout=5, poll_frequency=1):
        """定位多个元素"""
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll_frequency=1):
        """点击元素"""
        self.search_ele(loc, timeout, poll_frequency).click()

    def send_ele(self, loc, text, timeout=5, poll_frequency=1):
        """输入方法"""
        ele = self.search_ele(loc, timeout, poll_frequency)
        ele.clear()
        ele.send_keys(text)
