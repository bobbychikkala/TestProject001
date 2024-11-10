



import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities import readProperties
from utilities.currentTime import getCurrentTime
from utilities.customLogger import LogGen


class Test_002_Login():
    baseURL =   readProperties.ReadConfig.getApplicationURL()
    email   =   readProperties.ReadConfig.getEmail()
    password=   readProperties.ReadConfig.getPassword()

    logger = LogGen.loggen()

     
    @pytest.mark.sanity
    def test_login(self, setup: WebDriver):
       self.driver = setup
       self.driver.get(self.baseURL)
       self.logger.info(" *** Starting test_002_login ***")
       self.driver.maximize_window()

       self.driver.implicitly_wait(3)
       self.hp = HomePage(self.driver)
       
       self.hp.clickMyAccount()
       self.hp.clickLogin()
       self.driver.implicitly_wait(3)

       self.loginPage = LoginPage(self.driver)

       self.loginPage.setEmail(self.email)

       self.loginPage.setPassword(self.password)

       self.loginPage.click_Login()

       time.sleep(6)
       self.loginSuccessCnf = self.loginPage.getLoginCnf()
       print(self.loginSuccessCnf)

       if self.loginSuccessCnf == True :#'My Account':
            assert True
            self.logger.info('*** test_002_login test is passed  ****')
       else:
            ct = getCurrentTime()
            print(ct)
            self.driver.save_screenshot(f'D:\\pythonWS\\Project_001\\screenshots\\login{ct}.png')
            self.logger.error('*** test_002_login test is failed  ****')
            assert False
       self.logger.info('*** test_002_login test is finished  ****')
       self.driver.close()
        
    


