import sys
from time import sleep
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#PROFILE_URL = sys.argv[1]
PROFILE_URL = "https://www.tiktok.com/@b1ackh0le"

url_check = urlparse(PROFILE_URL)
#Check if url points to tiktok and to a profile. 
if(url_check.netloc != 'www.tiktok.com' or url_check.path[:2] != '/@'):
    sys.exit("URL is not for a profile!")

#Start DevTools ChromeDriver
service = Service('chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get(PROFILE_URL)

#Find all Videos on Users' Profile
video_elements = (driver.find_elements(by=By.CSS_SELECTOR, value=".tiktok-x6y88p-DivItemContainerV2"))
action = ActionChains(driver)
vid_list = []

#Todo manipulate elements to DL videos 
for video in video_elements:
    action.move_to_element(video).perform()
    print("At element", video)
    #vid_list.append = driver.find_element(by=By.CLASS_NAME, value="tiktok-lkdalv-VideoBasic e1yey0rl4")

driver.quit()
print(vid_list)