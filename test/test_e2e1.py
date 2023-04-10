import collections


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

from PageObject.CheckOut import checkouth
from PageObject.ConfirmPage import confirm
from PageObject.Homepage import HomePage
from test.baseclass import Baseclass


class Testone(Baseclass):

    def test_e2e1(self):

        self.driver.implicitly_wait(2)

        file_prod = []
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopitems()
        #checkoutpage = checkouth(self.driver)
        products = checkoutpage.carditems()

        for product in products:

            # file_prod.append(product.find_element(By.XPATH,"div/h4/a").text)
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == "Nokia Edge":
                product.find_element(By.CLASS_NAME, "btn-info").click()

        #self.driver.find_element(By.CSS_SELECTOR, "a[class = 'nav-link btn btn-primary']").click()
        checkoutpage.finalButton().click()
        #self.driver.find_element(By.CSS_SELECTOR, "button[class*='success']").click()
        checkoutpage.checkfinalfun().click()

        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifylinktext("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        #self.driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
        confirmvar = confirm(self.driver)
        confirmvar.checkbox().click()
        confirmvar.confirmsubmit().click()
        #self.driver.find_element(By.CSS_SELECTOR, "input[type = 'submit']").click()
        final_stat = self.driver.find_element(By.CSS_SELECTOR, "div[class*= 'alert-dismissible']").text
        assert "Success!" in final_stat
