from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self, url):
        self.driver.get(url)
        # ждём, пока появится поле логина
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME)
        )

    def login(self, username="", password=""):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.USERNAME)
        )
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PASSWORD)
        )

        username_input.clear()
        password_input.clear()

        username_input.send_keys(username)
        password_input.send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_text(self):
        error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error.text