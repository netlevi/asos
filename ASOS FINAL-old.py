#Initial setup
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
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
        delay = row[1]
        username = row[2]
        password = row[3]
        cvv = row[7]
refresh_time_in_seconds = 0.2
chrome_options = Options()  
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--window-size=800,600')
driver = webdriver.Chrome('D:\chromedriver.exe',options=chrome_options)
#driver = webdriver.Chrome('D:\chromedriver.exe')
#item URL
driver.get(url)
#select size
while True:
    try:
        driver.find_element_by_css_selector('#main-size-select-0')
        
    except NoSuchElementException:
        driver.refresh()
        time.sleep(refresh_time_in_seconds)
        
    else:
        select = Select(driver.find_element_by_id('main-size-select-0'))
        options = [o.text for o in select.options]
        option = random.choice(options)
        select.select_by_visible_text(option)
        wait = WebDriverWait(driver, 0.2)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-add"]/div/a/span[2]')))
        element.click()
        time.sleep(0.1)


#        driver.find_element_by_css_selector('#product-add > div > a > span:nth-child(2)').click()
#        
#Click Checkout

