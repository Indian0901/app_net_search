import sys,os
sys.path.append(os.getcwd())

from Base.initdriver import get_driver
from Base.page import Get_obj
import pytest,allure


class Test_net:
    def setup_class(self):
        self.driver = get_driver('com.android.settings','.Settings')
        self.get_obj = Get_obj(self.driver)
    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope='class',autouse=True)
    def go_net(self):
        self.get_obj.set_obj().more_btn()
        self.get_obj.more_obj().net_btn()
    @allure.step(title= "1设置网络模式")
    def test_net(self):
        self.get_obj.net_obj().one_btn(1)
        assert '3G' in self.get_obj.net_obj().res_list()






