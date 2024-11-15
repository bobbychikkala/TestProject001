import time

import pytest

from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from pageObjects.PcPage import PcPage
from utilities.customLogger import LogGen



class Test_004_PC:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.run(order=1)
    @pytest.mark.regression
    def test_004_Pc(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("*** --Test004-- Application Launching Started ***")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.hp =HomePage(self.driver)
        self.driver.implicitly_wait(5)
        self.logger.info("*** --Test004-- Moving on Desktop ***")
        self.logger.info("*** --Test004-- Clicking on PC ***")
        self.hp.clcikPcBtn()

        self.pcp = PcPage(self.driver)
        self.driver.implicitly_wait(3)

        if self.pcp.isPcPageDispalyed():
            self.logger.info("*** --Test004-- is Passed")
            assert True
        else:
            self.logger.error("*** --Test004-- is Failed")
            assert False
        self.driver.close()