import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# File Name
#FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")

# set driver and url
op = Options()
op.add_argument('--ignore-certificate-errors')
op.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=op)

for i in range(287):
    fname = str(i+1)+".png"
    url = 'http://127.0.0.1:5500/oekaki_area_checker.html?game='+str(i+1)
    driver.get(url)

    # get width and height of the page
    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")

    # set window size
    driver.set_window_size(400,830)
    FILENAME = os.path.join('C:/Users/boyage/OneDrive/Desktop/hp/game/static/images/img/game/ss_img',fname)
    # Get Screen Shot
    driver.save_screenshot(FILENAME)

# Close Web Browser
driver.quit()