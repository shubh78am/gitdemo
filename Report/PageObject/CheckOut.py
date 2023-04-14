from selenium.webdriver.common.by import By


class checkouth:

    def __init__(self, driver):
        self.driver = driver



    #self.driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")
    card = (By.XPATH, "//div[@class = 'card h-100']")

    #self.driver.find_element(By.CSS_SELECTOR, "a[class = 'nav-link btn btn-primary']").click()
    finalselection = (By.CSS_SELECTOR, "a[class = 'nav-link btn btn-primary']")

    #self.driver.find_element(By.CSS_SELECTOR, "button[class*='success']").click()
    checkfinal = (By.CSS_SELECTOR, "button[class*='success']")

    def carditems(self):
        return self.driver.find_elements(*checkouth.card)

    def finalButton(self):
        return self.driver.find_element(*checkouth.finalselection)


    def checkfinalfun(self):
        return self.driver.find_element(*checkouth.checkfinal)




