from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.google.com/maps")
driver.implicitly_wait(1000)

S_K = str('Mercedes-benz tokyo')

driver.find_element_by_css_selector('#searchboxinput').send_keys(S_K, Keys.ENTER)
driver.implicitly_wait(1000)

S_R = driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')

print(S_R)

time.wait(100)
