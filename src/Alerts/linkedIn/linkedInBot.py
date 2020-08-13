from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os, time, socket, re
from utils import checkInternetConnectivity
from django.conf import settings
from selenium.common.exceptions import TimeoutException

config = settings.CONFIG

class linkedInScraper:

    def __init__(self, website='linkedIn', driver = 'chromeDriver'):
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
        self.driver =  webdriver.Chrome(config.get(driver).get('path'), options = chromeOptions)

    def addDelay(self,timeInSeconds = 1):
        time.sleep(timeInSeconds)

    def login(self):
        if not checkInternetConnectivity:
            return
        self.driver.get(self.url)
        email = self.driver.find_element_by_name("session_key")
        password = self.driver.find_element_by_name("session_password")

        email.send_keys(self.email)
        self.addDelay(3)
        password.send_keys(self.password)
        self.addDelay(3)
        password.send_keys(Keys.ENTER)

    def getNotifications(self):
        notifications = []
        if not checkInternetConnectivity:
            return notifications
        self.login()
        self.addDelay(8)
        self.driver.get(self.url + 'notifications')
        self.addDelay(4)
        element = self.driver.find_element_by_class_name('core-rail')
        html = element.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        soup = soup.find('section')
        html = soup.findAll('div', id = re.compile('^ember\d+'), recursive = False)
        print(len(html))
        for element in html:
            if element.article is None or element.article.div is None:
                continue
            div = element.article.div
            divs = div.findAll('div', recursive = False)

            imageDiv = divs[0]
            img = imageDiv.find('img')
            if img == None:
                continue
            contentDiv = divs[1]
            words = contentDiv.findAll(text = True)
            words = [word for word in words if word not in (' ', '\n')]
            content = ''.join(map(str,words))

            date = divs[2].findAll('p')[-1]
            date = date.get_text(strip = True)
            notifications.append({'image': img['src'], 'body':content, 'created':date})

        self.driver.quit()
        return notifications