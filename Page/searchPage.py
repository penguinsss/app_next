from selenium.webdriver.common.by import By

from Base.base import Base


class SearchPage(Base):   # 继承
    def __init__(self, driver):
        Base.__init__(self, driver)
        self.search_btn = (By.ID, 'com.android.settings:id/search')
        self.search_text = (By.ID, 'android:id/search_src_text')
        self.search_result = (By.ID, 'com.android.settings:id/title')

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_ele(self.search_btn)

    def search_text_value(self, text):
        """搜索内容"""
        self.send_ele(self.search_text, text)

    def get_search_result(self):
        """获取搜索结果"""
        return [i.text for i in self.search_eles(self.search_result)]
