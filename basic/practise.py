import pytest
from util import get_driver


@pytest.fixture(params=['i', 'love', '你'])
def data(request):
    return request.param


class Test:
    @classmethod
    def setup_class(cls):
        cls.driver = get_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.fixture(scope='class', autouse=True)
    def go_sms(self):
        # 新建短信
        self.driver.find_element_by_id("com.android.mms:id/action_compose_new").click()
        # 输入手机号码
        self.driver.find_element_by_id("com.android.mms:id/recipients_editor").send_keys('1')

    def test(self, data):
        msg_edit = self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor")
        send = self.driver.find_element_by_id("com.android.mms:id/send_button_sms")
        msg_edit.send_keys(data)
        send.click()

        # 判断是否发送成功
        results = self.driver.find_elements_by_id("com.android.mms:id/text_view")
        assert data in [i.text for i in results]
