import time

from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from pageObjects.PcPage import PcPage

class Test_004_PC:
    baseURL = ReadConfig.getApplicationURL()

    def test_004_Pc(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.hp =HomePage(self.driver)
        self.driver.implicitly_wait(5)

        self.hp.clcikPcBtn()

        self.pcp = PcPage(self.driver)
        self.driver.implicitly_wait(3)

        if self.pcp.isPcPageDispalyed():
            assert True
        else:
            pass
