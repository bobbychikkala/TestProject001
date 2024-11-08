from selenium.webdriver.common.by import By


class AccountRegistrationPage():

    txt_firstname_xpath     =       '//*[@name="firstname"]'
    txt_lasttname_xpath     =       '//*[@name="lastname"]'
    txt_Email_xpath         =       '//*[@name="email"]'
    txt_Telephone_xpath         =       '//*[@name="telephone"]'
    txt_Password_xpath      =       '//*[@name="password"]'
    txt_Cnf_Password_xpath  =       '//*[contains(@name,"confirm")]'
    rd_Subsribe_xpath       =       '//*[@name="newsletter" and @value =1]'
    chk_Agree_xpath         =       '//*[@name="agree"]'
    btn_Continue            =       '//*[@value="Continue"]'
    txt_msg_confirm_xpath   =       '//*[@id="content"]/h1'


    def __init__(self,driver):
        self.driver         =       driver

    
    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(fname)
    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txt_lasttname_xpath).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_Email_xpath).send_keys(email)
    def setTelephone(self,telephone):
        self.driver.find_element(By.XPATH,self.txt_Telephone_xpath).send_keys(telephone)
    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_Password_xpath).send_keys(pwd)
    def setCnfPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_Cnf_Password_xpath).send_keys(pwd)
    def clickSubscribe(self):
        self.driver.find_element(By.XPATH,self.rd_Subsribe_xpath).click()
    def clickAgree(self):
        self.driver.find_element(By.XPATH,self.chk_Agree_xpath).click()
    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_Continue).click()

    def getConfirmation(self):
        try:
            confirmationMsg =  self.driver.find_element(By.XPATH,self.txt_msg_confirm_xpath ).text
            return confirmationMsg
        except:
            None
