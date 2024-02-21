import logging
import time



from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger()


class LoginLogout:

    def __init__(self, driver, base_url, username, password):
        self.driver = driver
        self.base_url = base_url
        self.username = username
        self.password = password
        # URL
        self.url_login = f'{self.base_url}/accounts/login/'
        # locators
        self.btn_sign_in_nav = '[id="log-in-link"]'
        self.field_username = '[name="login"]'
        self.field_password = '[name="password"]'
        self.btn_sign_in = '[type="submit"]'
        self.link_forgot_password = '[id="id_password_helptext"]'

        # users locators
        self.alert_signed_in ='[class="alert alert-dismissible alert-success"]'
        # logout page
        self.url_logout = f'{self.base_url}/accounts/logout/'
        self.bnt_sign_out = '[type="submit"]'
        self.alert_signed_out ='[class="alert alert-dismissible alert-success"]'
        # Expectations
        self.expectation_successful_alert_log_in = f"Successfully signed in as {self.username}."
        self.expectation_successful_alert_log_out = "You have signed out."


    def sign_in(self):
        logger.info('----- Auth user -----')
        self.driver.get(self.base_url)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_sign_in_nav).click()
        self.driver.get(self.url_login)
        self.driver.find_element(By.CSS_SELECTOR, self.field_username).send_keys(self.username)
        self.driver.find_element(By.CSS_SELECTOR, self.field_password).send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_sign_in).click()
        actual = self.driver.find_element(By.CSS_SELECTOR, self.alert_signed_in).text
        assert actual == self.expectation_successful_alert_log_in
        logger.info('----- User authorized -----')

    def sign_out(self):
        logger.info('----- Log out  -----')
        self.driver.get(self.url_logout)
        self.driver.find_element(By.CSS_SELECTOR, self.bnt_sign_out).click()
        actual = self.driver.find_element(By.CSS_SELECTOR, self.alert_signed_out).text
        assert actual == self.expectation_successful_alert_log_out
        logger.info('----- User Logged out  -----')

    def validate_forgot_password_page(self):
        logger.info('----- Log out  -----')
        self.driver.get(self.url_logout)
        self.driver.find_element(By.CSS_SELECTOR, self.bnt_sign_out).click()
        actual = self.driver.find_element(By.CSS_SELECTOR, self.alert_signed_out).text
        assert actual == self.expectation_successful_alert_log_out
        logger.info('----- User Logged out  -----')