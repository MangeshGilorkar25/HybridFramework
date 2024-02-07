import pytest
from selenium import webdriver

from utils import read_utils


class WebDriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.json_config=read_utils.get_json_as_dic(json_location="../test_data/config.json")
        browser = self.json_config["browser"]
        if browser == "ff":
            self.driver = webdriver.Firefox()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.json_config["url"])
        yield
        self.driver.quit()
