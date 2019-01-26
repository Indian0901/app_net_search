from Base.base_net import Base_net
import Page

class Page_search(Base_net):
    def __init__(self,driver):
        Base_net.__init__(self,driver)

    def send_text(self,text):
        self.send_element(Page.text_id,text)

    def res_list(self):
        return [i.text for i in self.search_elements(Page.res_id2)]