import pytest
from Base.getDriver import get_android_driver
from Page.searchPage import SearchPage


def data():
    return [('1', '休眠'), ('m', 'MAC地址'), ('w', 'WPS按钮')]


class Test_Search:
    def setup_class(self):
        self.driver = get_android_driver('com.android.settings', '.Settings')
        self.search_page = SearchPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope='class', autouse=True)
    def go_to_search(self):
        self.search_page.click_search_btn()

    @pytest.mark.parametrize('key, res', data())
    def test_001(self, key, res):
        self.search_page.search_text_value(key)
        assert res in self.search_page.get_search_result()
