import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

options = Options()
options = webdriver.ChromeOptions()

url = 'https://www.coupang.com/'

driver = webdriver.Chrome("./chromedriver.exe")
# driver = webdriver.Chrome("./chromedriver", chrome_options=options)

#Debuging mode
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
            """
})

driver.get(url)
time.sleep(2)
#driver.implicitly_wait(3)clickable로 나중에 변경``

driver.find_element_by_class_name('coupang-search').send_keys('닭가슴살')
driver.find_element_by_class_name('coupang-search').send_keys(Keys.ENTER)

time.sleep(2)