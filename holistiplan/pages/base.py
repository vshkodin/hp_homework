import logging
import time



from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from holistiplan.pages.login_logout import LoginLogout
from holistiplan.pages.home import Home
from holistiplan.pages.profile import Profile
from holistiplan.pages.signup import Signup


logger = logging.getLogger()


class Base:

    def __init__(self, driver, base_url, username, password):
        self.driver = driver
        self.base_url = base_url
        self.username = username
        self.password = password
        self.login_logout = LoginLogout(driver, base_url, username, password)
        self.home = Home(driver, base_url, username, password)
        self.profile = Profile(driver, base_url, username, password)
        self.signup = Signup(driver, base_url, username, password)
