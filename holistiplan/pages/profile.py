import logging
import time



from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger()


class Profile:

    def __init__(self, driver, base_url, username, password):
        self.driver = driver
        self.base_url = base_url
        self.username = username
        self.password = password
        self.test_name = "Rob"


        # locators profile page
        self.url_profile = f'{self.base_url}/users/1/"'
        self.btn_profile = '[href="/users/1/"]'
        self.btn_update = '[href="/users/~update/"]'
        self.btn_submit = '[type="submit"]'
        self.field_name = '[name="name"]'
        self.alet = '[class="alert alert-dismissible alert-success"]'
        self.expected_confirmation = 'Information successfully updated'





    def update_name_of_user(self):
        logger.info('----- try to update username -----')
        self.driver.find_element(By.CSS_SELECTOR, self.btn_profile).click()
        self.driver.find_element(By.CSS_SELECTOR, self.btn_update).click()
        self.driver.find_element(By.CSS_SELECTOR, self.field_name).click()
        self.driver.find_element(By.CSS_SELECTOR, self.field_name).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.field_name).send_keys(self.test_name)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_submit).click()
        alert = self.driver.find_element(By.CSS_SELECTOR, self.alet).text
        assert alert == self.expected_confirmation
        logger.info('----- username is updated -----')

