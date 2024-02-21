import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import page classes for structured page object model
from holistiplan.pages.login_logout import LoginLogout
from holistiplan.pages.home import Home
from holistiplan.pages.profile import Profile
from holistiplan.pages.signup import Signup

# Initialize logger for the class
logger = logging.getLogger(__name__)


class Base:
    """
    Base class for initializing page objects and providing shared attributes and methods.
    """

    def __init__(self, driver, base_url, username, password):
        """
        Initializes the Base class with common attributes and page objects.

        :param driver: WebDriver instance for browser interactions.
        :param base_url: Base URL of the website to test.
        :param username: Username for login.
        :param password: Password for login.
        """
        # Logging initialization of the Base class
        logger.info("Initializing Base class with user: %s", username)

        self.driver = driver
        self.base_url = base_url
        self.username = username
        self.password = password

        # Initialize page objects
        self.login_logout = LoginLogout(driver, base_url, username, password)
        self.home = Home(driver, base_url)
        self.profile = Profile(driver, base_url)
        self.signup = Signup(driver, base_url, username, password)

        # Logging successful initialization of page objects
        logger.info("Page objects initialized: LoginLogout, Home, Profile, Signup")

# Additional methods for the Base class would follow here...
