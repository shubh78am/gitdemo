from selenium.webdriver.common.by import By


class confirm:

    def __init__(self,driver):
        self.driver = driver

    #self.driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
    check = (By.XPATH, "//div[@class = 'checkbox checkbox-primary']")
    #self.driver.find_element(By.CSS_SELECTOR, "input[type = 'submit']").click()
    submit = (By.CSS_SELECTOR, "input[type = 'submit']")

    def checkbox(self):
        return self.driver.find_element(*confirm.check)



    def confirmsubmit(self):
        return self.driver.find_element(*confirm.submit)

