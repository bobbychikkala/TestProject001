import os
import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from utilities.readProperties import ReadConfig
from utilities.XLutils import Rd_excel
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage


class Test_003_MyAccount_DTT():
    baseURL = ReadConfig.getApplicationURL()

    lst_result = []
    xlpath = os.path.abspath(os.curdir) + "\\testData\\testData.xlsx"
    sheet = "Sheet1"
    data_excel = Rd_excel(xlpath, sheet)

    @pytest.mark.regression
    @pytest.mark.run(order=2)
    def test_003(self, setup: WebDriver):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(0)
        self.driver.implicitly_wait(5)

        ##Calling Home Page class(object)
        self.hp = HomePage(self.driver)

        self.driver.implicitly_wait(3)

        ## calling login page calss
        self.loginPage = LoginPage(self.driver)
        ##calling My account class
        self.ma = MyAccountPage(self.driver)
        self.rows = self.data_excel.getRowCont()

        for r in range(2, self.rows + 1):

            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.loginPage.setEmail(self.data_excel.readData(r, 2))

            self.loginPage.setPassword(self.data_excel.readData(r, 3))

            self.expect = self.data_excel.readData(r, 4)

            self.loginPage.click_Login()

            self.driver.implicitly_wait(3)

            time.sleep(0)

            if self.expect == "valid":

                if self.loginPage.getLoginCnf():

                    self.lst_result.append("Pass")
                    #self.hp.clickMyAccount()
                    time.sleep(1)
                    self.ma.click_Logout()
                else:
                    self.lst_result.append("Fail")
            elif self.expect == "invalid":
                if self.loginPage.getLoginCnf():
                    self.lst_result.append("Fail")
                    self.ma.click_Logout()
                else:
                    self.lst_result.append("Pass")

        if "Fail" not in self.lst_result:
            assert True
        else:
            assert False
        self.driver.close()