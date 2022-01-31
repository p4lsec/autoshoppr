from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle
import configparser

class AmazonLogin:
    def __init__(self, driver=None):
        self.url = "https://www.amazon.com/your-account"
        if driver is not None:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
    
    def login(self):
        try:
            self.driver.get(self.url)
            self.load_cookies()
            self.driver.find_element_by_xpath("//*[contains(text(), 'Login & security')]").click()
            config = configparser.ConfigParser()
            config.read('shoppr.conf')
        except:
            raise Exception("Could not add to cart")
  
    def load_cookies(self):
            cookies = pickle.load(open("amazon.pkl", "rb"))
            for cookie in cookies: 
                self.driver.add_cookie(cookie)