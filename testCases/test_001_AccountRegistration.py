from datetime import *
import warnings
import time
import os
from utilities import readProperties
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
from utilities.currentTime import getCurrentTime
from utilities.customLogger import LogGen
from utilities.randomString import random_string
import pytest

class Test_001_AccountReg:
    baseURL         =      readProperties.ReadConfig.getApplicationURL()

    logger  =   LogGen.loggen()



    @pytest.mark.run(order=4)
    @pytest.mark.sanity
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
        # pytest --html=reports_/report.html --self-contained-html

        print(self.confMsg)
        if self.confMsg == 'Your Account Has Been Created!':
            self.logger.info("*** Account Registration Test is passed ***")
            assert 1 == 1
        else:
            ct = getCurrentTime()
            file = os.path.abspath(os.curdir)+f'\\screenshots\\Test_001_AccReg{ct} .png'
            self.driver.save_screenshot(file)
            self.logger.error("*** Account Registration Test is Failed *** ")
            assert False
        
        self.driver.close()
        self.logger.info('*** test_001_Account Registartion Test is finished ***')