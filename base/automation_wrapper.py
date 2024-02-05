import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


class WebDriverWrapper:
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
