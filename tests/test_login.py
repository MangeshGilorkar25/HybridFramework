import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.automation_wrapper import WebDriverWrapper


class TestLogin(WebDriverWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.ID, "authUser").send_keys("admin")
        self.driver.find_element(By.ID, "clearPass").send_keys("pass")
        self.driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        actual_title = self.driver.title
        assert_that("OpenEMR Login").is_equal_to(actual_title)


class TestLoginUI(WebDriverWrapper):

    def test_title(self):
        print(self.a)
        print(self.driver)
        self.driver.implicitly_wait(5)
        actual_title = self.driver.title
        # assert_that("OpenEMR Login").is_equal_to(actual_title)
        assert_that(actual_title).contains("OpenEMR Login")

    def test_app_description(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        print(self.name)
        assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")

    def test_placeholder(self):
        actual_placeholder_username = self.driver.find_element(By.XPATH, "//input[@id='authUser']").get_attribute(
            "placeholder")
        actual_placeholder_password = self.driver.find_element(By.XPATH, "//input[@id='clearPass']").get_attribute(
            "placeholder")
        assert_that("Username").is_equal_to(actual_placeholder_username)
        assert_that("Password").is_equal_to(actual_placeholder_password)
