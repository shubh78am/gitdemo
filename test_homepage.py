import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.Homepage import HomePage
from TestData.HomepageTestData import HomePageTestData
from test.baseclass import Baseclass


class TestHomepage(Baseclass):

    def test_submission(self, getdata):
        # driver.find_element(By.NAME, "name").send_keys("shubham khare")
        self.driver.refresh()
        log = self.test_logging12()
        homepage = HomePage(self.driver)
        log.info("My First name is "+getdata["firstname"])
        homepage.Form_name().send_keys(getdata["firstname"])
        # self.driver.find_element(By.NAME, "email").send_keys("shubham@gmail.com")
        log.info("My lastname is "+getdata["lastname"])
        homepage.Form_email().send_keys(getdata["lastname"])
        # self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234565")
        homepage.Form_password().send_keys(getdata["password"])
        # self.driver.find_element(By.ID, "exampleCheck1").click()
        homepage.form_checkingbox().click()

        dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        # dropdown.select_by_index(1)
        dropdown.select_by_visible_text(getdata["gender"])

        # self.driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

        homepage.Form_submission().click()
        # wait = WebDriverWait(driver, 7)
        alerttext = self.driver.find_element(By.CSS_SELECTOR, "div[class*= 'alert-dismissible']").text
        # driver.find_element(By.CSS_SELECTOR, "div[class*= 'alert-dismissible']").text
        # print(driver.title)
        # print(driver.current_url)
        # driver.close()
        assert "success" in alerttext
        assert "success in githum demo line1" in alerttext
        assert "success in githum demo line2" in alerttext
        assert "success in githum demo line3" in alerttext
        assert "success in githum demo line4" in alerttext
        self.driver.refresh()

    #@pytest.fixture(params=[("shubham", "khare@mail.com", "123432443","Male"),
     #                       ("riti", "sri@mail.com", "32342434","Female")])
    @pytest.fixture(params= HomePageTestData.HomePage_TestData)
    def getdata(self, request):
        return request.param
