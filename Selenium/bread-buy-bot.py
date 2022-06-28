from cgitb import html
from bs4 import BeautifulSoup
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
import soupsieve

driver = webdriver.Chrome("./chromedriver")

# driver.get("http://janginthe.com/product/%EC%9E%A5%EC%9D%B8%EB%8D%94-%EC%95%BD%EA%B3%BC%EB%B9%B5/258/category/24/display/1/")

driver.get("http://janginthe.com/product/%EC%9D%98%EC%A0%95%EB%B6%80-%EC%9E%A5%EC%9D%B8%ED%95%9C%EA%B3%BC-%EB%AA%BB%EB%82%9C%EC%9D%B4-%EC%95%BD%EA%B3%BC-%ED%8C%8C%EC%A7%80%EC%95%BD%EA%B3%BC/260/category/24/display/1/")
driver.implicitly_wait(1000)

#빵 갯수를 입력해주세요.
num_of_ppang = 2

#아이디와 비번을 입력해주세요.
id = "ID"
password = "Password#"
#주소를 미리 마이페이지에서 입력 해놔 주세요 ( 안그러면 안댐 )
#장바구니에 있는 제품은 미리 삭제해놔 주세요 ( 안그러면 오류남 )

driver.find_element_by_css_selector("#header > div.inner > div > div > ul.xans-element-.xans-layout.xans-layout-statelogoff.right.off > li:nth-child(1) > a").click()
driver.find_element_by_name('member_id').send_keys(id)
driver.find_element_by_name('member_passwd').send_keys(password)
driver.find_element_by_name('member_passwd').send_keys(Keys.ENTER)

driver.implicitly_wait(10000)
# ppang = num_of_ppang -1 

# for i in range(ppang):
    
#     driver.find_element_by_css_selector("#totalProducts > table > tbody:nth-child(4) > tr > td:nth-child(2) > span > a.up.QuantityUp > img").click()

driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[2]/div[2]/div[6]/div[1]/a[1]').click()
driver.implicitly_wait(10000)
driver.find_element_by_xpath('//*[@id="btn_payment"]').click()
driver.implicitly_wait(100)
driver.find_element_by_css_selector("#stdPaymentConfirmView > div.pgmBtnArea > a > img").click()

#여기서 결제창이 나옴
driver.implicitly_wait(10000)
print(driver.window_handles)

window_before = driver.window_handles[0]

window_after = driver.window_handles[1]

driver.switch_to.window(window_after)

# driver.implicitly_wait(10000)

# html = driver.page_source
# soup = bs4.BeautifulSoup(html, 'html.parser')
# notices = soup.select('#container > div.incont > div.contents')

# for n in notices:
#     print(n.text.strip())

#element = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[3]/div[1]/span')
#driver.execute_script("arguments[0].click();", element)
#driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[3]/div[2]/a[2]').click()
#driver.find_element_by_xpath('//*[@id="027"]').click()
#driver.find_element_by_xpath('//*[@id="div_cardArea"]/div[8]/a[2]').click()
#driver.find_element_by_xpath('//*[@id="contents"]/ul/li[1]/a').click()

time.sleep(10000)
