from dotenv import load_dotenv
import os
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "BROWSERSTACK_USERNAME"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "BROWSERSTACK_ACCESS_KEY"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"

bstack_options = {
    "os" : "OS X",
    "osVersion" : "Monterey",
    "buildName" : "youtube video downloader test",
    "sessionName" : "test build 1 for youtube downloader",
    "userName": BROWSERSTACK_USERNAME,
    "accessKey": BROWSERSTACK_ACCESS_KEY
}
bstack_options["source"] = "python:sample-main:v1.0"
options = ChromeOptions()
options.set_capability('bstack:options', bstack_options)
driver = webdriver.Remote(
    command_executor=URL,
    options=options)
driver.get("https://youtubemp6.vercel.app")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_id("input").send_keys("https://www.youtube.com/watch?v=GfsAGREha6o")
driver.find_element_by_id("submit").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div/div/div[1]/a/button").click()

driver.implicitly_wait(2)
driver.get_screenshot_as_png()
driver.get_screenshot_as_file("screenshot.png")

driver.quit()