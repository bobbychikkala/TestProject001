from selenium.webdriver.common.by import By



class MyAccountPage:
    btn_logout_xpath = "//*[contains(text(),'Logout')]"




    def __init__(self,driver):
        self.driver  =  driver


    def click_Logout(self):

        self.driver.find_element(By.XPATH , self.btn_logout_xpath).click()


    