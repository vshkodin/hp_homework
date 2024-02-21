import logging
import time



from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger()


class Signup:

    def __init__(self, driver, base_url, username, password):
        self.driver = driver
        self.base_url = base_url
        self.username = username
        self.password = password


        # locators signup page
        self.bnt_sign_up_nav_panel = '[id="sign-up-link"]'
        self.field_email = '[name="email"]'
        self.field_password1 = '[name="password1"]'
        self.field_password2 = '[name="password2"]'
        self.bnt_sign_up_submit = '[type="submit"]'
        self.lbl_confirmation_text = 'body > div:nth-child(3) > div > div > p'
        self.expectation_cinfirmation_text = 'We have sent an e-mail to you for verification. Follow the link provided to finalize the signup process. Please contact us if you do not receive it within a few minutes.'




    def sign_up(self):
        logger.info('----- sign_up user -----')
        self.driver.get(self.base_url)
        self.driver.find_element(By.CSS_SELECTOR, self.bnt_sign_up_nav_panel).click()
        self.driver.find_element(By.CSS_SELECTOR, self.field_email).send_keys(self.username)
        self.driver.find_element(By.CSS_SELECTOR, self.field_password1).send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, self.field_password2).send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, self.bnt_sign_up_submit).click()
        actual = self.driver.find_element(By.CSS_SELECTOR, self.lbl_confirmation_text).text
        assert actual == self.expectation_cinfirmation_text
        logger.info('----- User authorized -----')

