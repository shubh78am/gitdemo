from selenium.webdriver.common.by import By

from PageObject.CheckOut import checkouth


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    #driver.find_element(By.NAME, "name").send_keys("shubham khare")
    name = (By.NAME, "name")
    #driver.find_element(By.NAME, "email").send_keys("shubham@gmail.com")
    email = (By.NAME, "email")
    #driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234565")
    password = (By.ID, "exampleInputPassword1")
    #driver.find_element(By.ID, "exampleCheck1").click()
    checkingbox = (By.ID, "exampleCheck1")
    #driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
    submission = (By.XPATH, "//input[@type = 'submit']")

    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = checkouth(self.driver)
        return checkoutpage

    def Form_name(self):
        return self.driver.find_element(*HomePage.name)

    def Form_email(self):
        return self.driver.find_element(*HomePage.email)

    def Form_password(self):
        return self.driver.find_element(*HomePage.password)

    def form_checkingbox(self):
        return self.driver.find_element(*HomePage.checkingbox)

    def Form_submission(self):
        return self.driver.find_element(*HomePage.submission)

