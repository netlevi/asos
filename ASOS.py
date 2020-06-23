#Initial setup
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import random
with open('tasks.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    url = []
    size = []
    cvv = []
    username = []
    password = []
    for row in readCSV:
        url = row[0]
        size = row[1]
        username = row[2]
        password = row[3]
        cvv = row[7]
        
chrome_options = Options()  
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome('D:\chromedriver.exe',options=chrome_options)
#driver = webdriver.Chrome('D:\chromedriver.exe')
#item URL
driver.get(url)
#select size
try:
    element = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="product-size"]/section/div/div[1]/div[2]'))
    )
finally:
    select = Select(driver.find_element_by_xpath('//*[@id="main-size-select-0"]'))
    #driver.find_element_by_xpath('//*[@id="product-size"]/section/div/div[1]/div[2]').click()

options = [o.text for o in select.options]
#option = random.choice(options)
print ([o.text for o in select.options])
#select it
select.select_by_visible_text(size)
try:
    element = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="product-add"]/div/a/span[2]'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="product-add"]/div/a/span[2]').click()
#Click Checkout
print ('COOOOOOK!')


