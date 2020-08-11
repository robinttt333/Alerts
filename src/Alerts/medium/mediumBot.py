from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time
from utils import checkInternetConnectivity
from django.conf import settings

config = settings.CONFIG
class ScraperPersonal:
    
    def __init__(self, website='medium', driver = 'chromeDriver'):

        #website specific details
        self.url = config.get(website).get('url')
        self.email = config.get(website).get('email')
        self.password = config.get(website).get('password')

        #chrome specific details
        chromeOptions = Options()
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--disable-gpu")
        # chromeOptions.add_argument("--headless")
        
        #Chrome driver
        self.driver = webdriver.Chrome(config.get(driver).get('path'), options = chromeOptions)
    
    def addDelay(self,timeInSeconds = 1):
        time.sleep(timeInSeconds)

    def login(self):
        if not checkInternetConnectivity():
            return

        self.driver.get(self.url)
        self.driver.find_element_by_link_text("Sign in").click()
        signInUsingGmailButton = self.driver.find_elements_by_class_name("button-label")
        if len(signInUsingGmailButton) == 0:
            signInUsingGmailButton = self.driver.find_element_by_link_text("Sign in with Google")
        else :
            signInUsingGmailButton = signInUsingGmailButton[0]
        
        signInUsingGmailButton.click()
        email = self.driver.find_element_by_name("identifier")
        email.send_keys(self.email)
        email.send_keys(Keys.ENTER)
        
        self.addDelay(4)

        password = self.driver.find_element_by_name("password")
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)

    def getNotifications(self):
        if not checkInternetConnectivity():
            return
        self.login()
        self.addDelay(10)
        self.driver.find_element_by_xpath('//*[@title="Notifications"]').click()
