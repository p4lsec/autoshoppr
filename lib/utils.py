from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib import auth
import pickle

class AmazonShoppr:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.auth = auth.AmazonLogin(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        
    def login(self):
        try:
            self.auth.login()
        except:
            raise Exception("Could not login")
        
    def add_by_url(self, url, qty=None):
        try:
            add_to_cart_xpath = '//*[@id="freshAddToCartButton-announce"]'
            self.driver.get(url)
            if qty is not None:
                qty_xpath = '//*[@class="qs-widget-dropdown-item"]'
                self.click_by_xpath_webchains("//button[contains(text(),'Qty: 1')]")
                self.driver.find_elements_by_xpath(qty_xpath)[qty].click()
            self.click_by_xpath_webchains(add_to_cart_xpath)
        except:
            raise Exception("Could not add to cart")
       
    def clean_exit(self):
        '''
        Save cookies, close browser, and exit
        '''
        pickle.dump(self.driver.get_cookies(), open("amazon.pkl","wb"))
        self.driver.close()
        self.driver.quit()
        return
        
    def dirty_exit(self):
        '''
        Close browser and exit
        '''
        self.driver.close()
        self.driver.quit()
        return

    def click_by_xpath(self, xpath):
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
        return
    
    def click_by_xpath_webchains(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        webdriver.ActionChains(self.driver).move_to_element(element).click(element).perform()
        return