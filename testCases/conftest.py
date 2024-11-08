from datetime import datetime
import os
import pytest
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver



################## pytest HTML Report ###########

########### pytest HTML Report ################

#It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Opencart'
#     config._metadata['Module Name'] = 'CustRegistration'
#     config._metadata['Tester'] = 'Pavan'

# #It is hook for delete/Modify Environment info to HTML Report
# pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
    
#     metadata.pop("Plugins", None)

# #Specifying report folder location and save report with timestamp
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
    
#     config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d%m%y%H%M%S")+".html"

