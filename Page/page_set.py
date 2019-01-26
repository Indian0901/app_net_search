from Base.base_net import Base_net
import Page

class Page_set(Base_net):
    def __init__(self,driver):
        Base_net.__init__(self,driver)

    def more_btn(self):
        self.click_element(Page.more_xpath)

    #搜索
    def click_search(self):
        self.click_element(Page.search_id)