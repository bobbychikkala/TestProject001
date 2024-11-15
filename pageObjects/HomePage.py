import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



class HomePage:
    lnk_myaccount_xpath = '//span[contains(text(),"My Account")]'
    lnk_register_xpath     = '//a[contains(text(),"Register")]'
    lnk_login_xpath     =  '//a[contains(text(),"Login")]'
    btn_Desktop_xpath = '//*[text()="Desktops"]'
    btn_PC_xpath = '//*[text()="PC (0)"]'


    def __init__(self,driver):
        self.driver  =  driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.lnk_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.lnk_register_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.lnk_login_xpath).click()

    def clcikPcBtn(self):
        action = ActionChains(self.driver)
        action.reset_actions()
        self.ele_DeskTop = self.driver.find_element(By.XPATH,self.btn_Desktop_xpath)
        self.ele_PC = self.driver.find_element(By.XPATH,self.btn_PC_xpath)


        action.move_to_element(self.ele_DeskTop).click(self.ele_PC).perform()
        time.sleep(0)