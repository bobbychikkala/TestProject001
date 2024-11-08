
from selenium.webdriver.common.by import By

class LoginPage():

    txt_Email_xpath     =       '//*[@name="email"]'
    txt_Password_xpath  =       '//*[@name="password"]'
    btn_Login_xpath     =       '//*[@value="Login"]'
    cnf_login_xptha     =       '//*[@id="content"]/h2[1]'

    def __init__(self,driver):
        self.driver  =  driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txt_Email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txt_Password_xpath).send_keys(password)
    
    def click_Login(self):
        self.driver.find_element(By.XPATH,self.btn_Login_xpath).click()
    
    def getLoginCnf(self):
        try:
            self.loginCnfMsg = self.driver.find_element(By.XPATH,self.cnf_login_xptha).is_displayed()
            return self.loginCnfMsg
        except:
            None