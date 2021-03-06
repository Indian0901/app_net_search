import sys,os
sys.path.append(os.getcwd())

from Base.initdriver import get_driver
from Base.page import Get_obj
import pytest,allure
from Data.get_data import get_data

class Test_search:
    def setup_class(self):
        self.driver = get_driver('com.android.settings','.Settings')
        self.get_obj = Get_obj(self.driver)
    def teardown_class(self):
        self.driver.quit()



    @pytest.fixture(scope='class',autouse=True)
    def go_search(self):
        self.get_obj.set_obj().click_search()

    @allure.step(title="2搜索关键字并查看结果")
    @pytest.mark.parametrize('key,value', get_data())
    def test_search(self,key,value):
        self.get_obj.search_obj().send_text(key)
        assert value in self.get_obj.search_obj().res_list()




