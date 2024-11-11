
import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from utilities.readProperties import ReadConfig 
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage


class Test_003_MyAccount_DTT():

    baseURL = ReadConfig.getApplicationURL()
    email   = ReadConfig.getEmail()
    password = ReadConfig.getPassword()



    @pytest.mark.regression
    def test_003(self,setup: WebDriver):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        ##Calling Home Page class(object)
        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.driver.implicitly_wait(3)

        ## calling login page calss
        self.loginPage = LoginPage(self.driver)

        self.loginPage.setEmail(self.email)

        self.loginPage.setPassword(self.password)
 
        self.loginPage.click_Login()

        self.driver.implicitly_wait(3)

        ##calling My account class
        self.ma = MyAccountPage(self.driver)
        self.hp.clickMyAccount()
        self.ma.click_Logout()

        time.sleep(4)



        
        
        
        
        
        
        
        
        
        
        
        
        print('bobby')
        assert True
