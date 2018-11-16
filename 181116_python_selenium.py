


#%%
# selenium
from selenium import webdriver
import os
os.getcwd()

#%%
# driver
driver = webdriver.Chrome('chromedriver')
driver.get('https://goo.gl/VH1A5t')

#%%
gu_list_ele=driver.find_element_by_xpath('//*[@id="SIGUNGU_NM0"]')
gu_list_ele.send_keys('마포구')

#%%
gu_list_ele=driver.find_element_by_xpath('//*[@id="SIGUNGU_NM0"]')
gu_list=gu_list_ele.find_elements_by_tag_name('option')
gu_names=[option.get_attribute('value') for option in gu_list]
gu_names.remove('')
gu_names

#for option in gu_list:
#    print(option)
#%%
gu_names[1]

#%%
gu_list_ele=driver.find_element_by_xpath('//*[@id="SIGUNGU_NM0"]')
gu_list_ele.send_keys(gu_names[1])
xpath='//*[@id="searRgSelect"]/span' # 조회버튼 xpath

ele_search=driver.find_element_by_xpath(xpath).click

#%%
import time
from tqdm import tqdm_notebook

for gu in tqdm_notebook(gu_names):
    ele_gu = driver.find_element_by_id('SIGUNGU_NM0')
    ele_gu.send_keys(gu)
    time.sleep(3) # 3초 휴식
    
    xpath='//*[@id="searRgSelect"]/span' #조회버튼 xpath
    ele_search=driver.find_element_by_xpath(xpath).click()
    time.sleep(1) # 1초 휴식
    
    xpath='//*[@id="glopopd_excel"]/span' # 엑셀 저장 버튼
    ele_excel=driver.find_element_by_xpath(xpath).click()
    
    
    

