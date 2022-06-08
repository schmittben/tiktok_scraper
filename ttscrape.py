import sys
from time import sleep
from tkinter.tix import Select
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PROFILE_URL = sys.argv[1]

url_check = urlparse(PROFILE_URL)
#Check if url points to tiktok and to a profile. 
if(url_check.netloc != 'www.tiktok.com' or url_check.path[:2] != '/@'):
    sys.exit("URL is not for a profile!")

service = Service('chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get(PROFILE_URL)

video_elements = (driver.find_elements(by=By.CSS_SELECTOR, value=".tiktok-x6y88p-DivItemContainerV2"))

#Todo manipulate elements to DL videos 
for video in video_elements:
    print(video)