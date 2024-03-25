import requests
import selenium.common.exceptions
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from lxml import etree

# 不自动关闭浏览器
option =webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

def find_button_element():
    return driver.find_element(By.CLASS_NAME,"YSxEq5R4SeKN3kebhd4y")
#导入驱动
driver=webdriver.Chrome(option)
#https://top.chinaz.com/all/ 排名靠前的网站

web=[]
for i in range(1,51):
    if i==1:
        url="https://top.chinaz.com/all/index.html"
    else:
        url=f"https://top.chinaz.com/all/index_{i}.html"

    driver.get(url)
    list=driver.find_elements(By.XPATH,'//li[@class="clearfix  "]/div[2]/h3/span')#不能用text()
    for i in list:
        web.append(i.text)
dataframe=pd.DataFrame({'URL':web})
dataframe.to_csv('china_popular_web.csv',index=False)
#<li class="clearfix  ">