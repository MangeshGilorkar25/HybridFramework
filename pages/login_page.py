from selenium.webdriver.common.by import By
from assertpy import assert_that


class LoginPage:

    def __init__(self, driver):
        self.__driver = driver

    def enter_username(self, username):
        self.__driver.find_element(By.ID, "authUser").send_keys(username)

    def enter_password(self, password):
        self.__driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)

    # click on login

    def click_login(self):
        self.__driver.find_element(By.ID, "login-button").click()

    # get_error_message()
