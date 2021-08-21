from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-notifications")
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

chrome.get("https://popcat.click/")
target = chrome.find_element_by_xpath('//*[@id="app"]/div')

while(True):
    target.click()