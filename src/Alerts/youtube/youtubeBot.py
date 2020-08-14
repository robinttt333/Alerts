from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os, time, socket, re
from selenium.common.exceptions import TimeoutException
from django.conf import settings
from utils import checkInternetConnectivity

config = settings.CONFIG

class youtubeScraper:

    def __init__(self, website='youtube', driver = 'chromeDriver'):
        #website specific details
        self.url = config.get(website).get('url')
        self.alternateUrl = config.get(website).get('alternateUrl')
        self.email = config.get(website).get('email')
        self.password = config.get(website).get('password')

        #chrome specific details
        chromeOptions = Options()
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--disable-gpu")
        # chromeOptions.add_argument("--headless")

        #Chrome driver
        self.driver =  webdriver.Chrome(config.get('chromeDriver').get('path'), options = chromeOptions)

    def addDelay(self,timeInSeconds = 1):
        time.sleep(timeInSeconds)

    def alternateLogin(self, website = 'stackoverflow'):
        self.driver.get(self.alternateUrl)
        self.driver.find_element_by_link_text("Log in").click()
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        email = self.driver.find_element_by_name("identifier")
        email.send_keys(self.email)
        email.send_keys(Keys.ENTER)
        self.addDelay(4)
        password = self.driver.find_element_by_name("password")
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        self.addDelay(10)

        
    def login(self):
        if not checkInternetConnectivity():
            return
        self.alternateLogin()
        # self.driver.get(self.url)
        # self.addDelay(10)

    def getNotifications(self):
        if not checkInternetConnectivity():
            return
            
        self.login()
        self.driver.find_element_by_class_name("ytd-notification-topbar-button-renderer").click()
        self.addDelay(10)
        htmlElements = self.driver.find_elements_by_tag_name("ytd-notification-renderer")

        for html in htmlElements:
            soup = BeautifulSoup(html, 'html.parser')
            a = soup.find('a')

            newDiv = a.find("div", {"id" : "new"})
            read = False
            if newDiv is None:
                read = True

            image = a.find("yt-img-shadow").find("img")["src"]
            time = a.find("div", {"class" :"text"}).find("div", {"class" : "metadata"}).findAll("yt-formatted-string",recursive = False)[-1].get_text()
            text = a.find("div", {"class" :"text"}).find("yt-formatted-string").get_text()
            thumbnail = a.find("div",{"class": "thumbnail-container"}).find("img")['src']

            print(image,time,text,thumbnail)

        self.driver.quit()