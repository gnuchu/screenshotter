import os
import time
import io
import sqlite3
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

db = sqlite3.connect('db/speeds.sqlite3')
c = db.cursor()

now = datetime.now()
textdate = now.strftime('%d-%m-%Y %H:%M:%S')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(executable_path=os.path.abspath("driver/chromedriver.exe"), chrome_options=chrome_options)
driver.get("https://www.fast.com")
time.sleep(15)

magnifying_glass = driver.find_element_by_id("speed-value")
speed = magnifying_glass.get_attribute('innerHTML')

if speed == None:
  print("We didn't get a speed this time.")
else:
  sql = f"insert into speeds(speed, datetime) values ({speed}, '{textdate}')"
  c.execute(sql)
  
db.commit()
db.close()
driver.close()