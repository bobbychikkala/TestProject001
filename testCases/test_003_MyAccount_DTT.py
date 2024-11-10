
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
class Test_003_MyAccount_DTT():
    @pytest.mark.regression
    def test_003(self,setup: WebDriver):
        print('bobby')
        assert True
