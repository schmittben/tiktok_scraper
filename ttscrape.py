import sys
import requests
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

PROFILE_URL = sys.argv[1]

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

for video in video_elements:
    #Hovers over video on profile to activate Autoplay and grant access to mp4 file
    action.move_to_element(video).perform()
    print("At element", video)

    #Grabs video mp4 link and adds to video url list
    hover_vid = driver.find_element(by=By.CSS_SELECTOR, value=".tiktok-lkdalv-VideoBasic")
    vid_list.append(hover_vid.get_attribute('src') + ".mp4")

driver.quit()

#Download Videos
for index, video_url in enumerate(vid_list):
    fileName = "video_" + str(index) + ".mp4"
    vid_req = requests.get(video_url)
    with open("Downloads/" + fileName, "wb") as f:
        f.write(vid_req.content)
    f.close()