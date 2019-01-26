from selenium.webdriver.common.by import By

#修改网络
more_xpath = (By.XPATH,"//*[contains(@text,'更多')]")
net_xpath = (By.XPATH,"//*[contains(@text,'移动网络')]")
one_xpath = (By.XPATH,"//*[contains(@text,'首选')]")
numtype_xpath = (By.XPATH,"//*[contains(@text,'3G')]")
res_id = (By.ID,'android:id/summary')


#搜索
search_id = (By.ID,'com.android.settings:id/search')
text_id = (By.ID,'android:id/search_src_text')
res_id2 = (By.ID,'com.android.settings:id/title')
