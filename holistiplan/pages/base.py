import logging
import time



from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger()


class Base:

    def __init__(self, driver, base_url, username, password):
        self.driver = driver
        self.base_url = base_url
        self.username = username
        self.password = password

    def sign_in(self):
        logger.info('----- Auth user -----')
        self.driver.get(self.base_url)
        import time
        time.sleep(5)