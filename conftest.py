import pytest
import logging
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from holistiplan.pages.base import Base

with open('config.json') as config_file:
    config = json.load(config_file)

# Defineed command-line options for pytest
def pytest_addoption(parser):
    parser.addoption("--local", action="store_true", help="Enable the flag")


# Define a fixture to configure logging
@pytest.fixture(scope="session")
def logger():
    # Define the log file path
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)
    # Create a file handler to save logs to a file
    file_handler = logging.FileHandler("test_logs.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    # Add the file handler to the logger
    logger.addHandler(file_handler)
    return logger



# Define a fixture that will set up and tear down the driver
@pytest.fixture
def driver(request):
    service = ChromeService()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(20)
    yield driver
    # Quit the driver once all tests have been run
    driver.quit()


# Log information about running each test
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
    logger = logging.getLogger("test_logger")
    logger.info(f"Running test: {item.nodeid}")
    return None


# Log information about test outcomes
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    logger = logging.getLogger("test_logger")
    if rep.when == "call" and rep.failed:
        logger.error(f"Test failed: {item.nodeid}")
    if rep.when == "call" and rep.passed:
        logger.info(f"Test passed: {item.nodeid}")


# Define a fixture base page object
@pytest.fixture
def holistiplan(driver):
    holistiplan_instance = Base(driver, config['local_base_url'], config['local_username'], config['local_password'])
    return holistiplan_instance
