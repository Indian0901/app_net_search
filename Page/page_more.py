from Base.base_net import Base_net
import Page

class Page_more(Base_net):
    def __init__(self,driver):
        Base_net.__init__(self,driver)

    def net_btn(self):
        self.click_element(Page.net_xpath)