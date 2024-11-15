from selenium.webdriver.common.by import By


class PcPage:
    txt_PC_xpath = '//*[@id="content"]/h2'

    def __init__(self, driver):
        self.driver = driver

    def isPcPageDispalyed(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_PC_xpath).is_displayed()
        except:
            pass
