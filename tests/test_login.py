import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLoginUI:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.a = 10
        self.name = "Mangesh"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://demo.openemr.io/b/openemr")
        yield
        self.driver.quit()

    def test_title(self):
        print(self.a)
        print(self.driver)
        actual_title = self.driver.title
        assert_that("OpenEMR Login").is_equal_to(actual_title)

    def test_app_description(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        print(self.name)
        assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")

