from datetime import *

import time
import pytest


from utilities import readProperties
#from selenium.webdriver.chrome.webdriver import WebDriver

from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
from utilities.currentTime import getCurrentTime
from utilities.customLogger import LogGen
from utilities.randomString import random_string


class Test_001_AccountReg():
    baseURL         =      readProperties.ReadConfig.getApplicationURL()

    logger  =   LogGen.loggen()

    def test_account_reg(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info('*** test_001_Account Registartion started ***')

        

        self.hp   =  HomePage(driver=self.driver)
        
        self.driver.implicitly_wait(15)
        self.logger.info("*** Clicking on My Account ***")
        self.hp.clickMyAccount()
        self.driver.implicitly_wait(10)
        self.hp.clickRegister()

        self.regpage = AccountRegistrationPage(self.driver)
        self.logger.info("*** Providing Customer Details ***")
        time.sleep(2)
        self.regpage.setFirstName('Mitchel')
        self.regpage.setLastName('John')
        #self.regpage.setEmail('axbyaqz@gmail.com')
        self.regpage.setEmail(random_string(6)+'@gmail.com')
        self.regpage.setTelephone('7898456321')
        self.regpage.setPassword("ASDFLKJ")
        self.regpage.setCnfPassword("ASDFLKJ")
        self.regpage.clickSubscribe()
        self.regpage.clickAgree()
        self.regpage.clickContinue()
        time.sleep(2)
        self.confMsg = self.regpage.getConfirmation()

        print(self.confMsg)
        # pytest --html=reports/report.html --self-contained-html

        print(self.confMsg)
        if self.confMsg == 'Your Account Has Been Created!':
            self.logger.info("*** Account Registration Test is passed ***")
            assert True
        else:
            ct = getCurrentTime()
            self.driver.save_screenshot(f'D:\\pythonWS\\Project_001\\screenshots\\Test_AccReg{ct} .png')
            self.logger.error("*** Account Registration Test is Failed *** ")
            assert False
        
        self.driver.close()
        self.logger.info('*** test_001_Account Registartion Test is finished ***')
        
        




       


