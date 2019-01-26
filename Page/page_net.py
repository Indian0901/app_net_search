from Base.base_net import Base_net
import Page

class Page_net(Base_net):
    def __init__(self,driver):
        Base_net.__init__(self,driver)

    def one_btn(self,num):
        self.click_element(Page.one_xpath)
        if str(num) == '1':
            self.click_element(Page.numtype_xpath)

    def res_list(self):
        return [i.text for i in self.search_elements(Page.res_id)]