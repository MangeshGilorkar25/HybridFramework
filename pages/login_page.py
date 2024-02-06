from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.__driver = driver

    def enter_username(self, username):
        self.__driver.find_element(By.ID, "authUser").send_keys(username)

    def enter_password(self, password):
        self.__driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)

    def click_on_login(self):
        self.__driver.find_element(By.ID, "login-button").click()

    def get_error_message(self):
        return self.__driver.find_element(By.XPATH, "//p[contains(text(),'Invalid')]").text

    @property
    def get_login_title(self):
        return self.__driver.title

    @property
    def get_app_desc(self):
        return self.__driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text

    @property
    def get_username_placeholder(self):
        return self.__driver.find_element(By.ID, "authUser").get_attribute("placeholder")

    @property
    def get_password_placeholder(self):
        return self.__driver.find_element(By.CSS_SELECTOR, "#clearPass").get_attribute("placeholder")