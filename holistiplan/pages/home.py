import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger()


class Home:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url


        # locators
        self.add_15_points = '[class="link-dark"]'
        self.lbl_points_remain = '#points-status > div:nth-child(2) > div.row.justify-content-around > div:nth-child(2) > div.card-body'
        self.btn_redeem_points = 'body > div:nth-child(3) > div.row.mt-4 > div:nth-child(1) > div > div.card-body > div > div > a'

        self.btn_clear_points = '#alerts > div > span > a'
        self.btn_claim = '[class="btn btn-success btn-lg"]'
        self.alert = '[class="alert alert-dismissible alert-info"]'
        self.btn_hide_bar = '[id="djHideToolBarButton"]'
        # expectations
        self.expected_text = 'You successfully claimed the following rewards: Tote Bag of Holding'
        self.expected_points = "0"
        self.expected_points_2 = "10.25"
        self.expected_points_2 = "12.25"

    def redeem_points(self):
        logger.info('----- try to redeem points -----')
        self.driver.get(self.base_url)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_hide_bar).click()
        self.driver.find_element(By.CSS_SELECTOR, self.btn_clear_points).click()
        self.driver.find_element(By.CSS_SELECTOR, self.add_15_points).click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_redeem_points).click()
        from selenium.webdriver.common.keys import Keys
        self.driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        # element = self.driver.find_element(By.CSS_SELECTOR, '[class="navbar-toggler-icon"]')
        # self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_claim).click()
        alert = self.driver.find_element(By.CSS_SELECTOR, self.alert).text
        assert alert == self.expected_text
        logger.info('----- points redeemed -----')

    def clear_points(self):
        logger.info('----- try to clear points -----')
        self.driver.get(self.base_url)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_hide_bar).click()
        self.driver.find_element(By.CSS_SELECTOR, self.btn_clear_points).click()
        self.driver.find_element(By.CSS_SELECTOR, self.add_15_points).click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_clear_points).click()
        time.sleep(2)
        points = self.driver.find_element(By.CSS_SELECTOR, self.lbl_points_remain).text
        assert points == self.expected_points
        logger.info('----- points cleared -----')
