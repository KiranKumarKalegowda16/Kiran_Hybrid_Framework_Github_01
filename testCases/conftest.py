from selenium import webdriver
from configurations.config import Config
from utilities.webdriverCore import browser_options,get_driver
from utilities.customLogger import LogGeneration
from time import sleep
import pytest

driver = None

""" Code to launch required browser by calling it's name in command line by passing browser nane as arguments and also launching broswer in headless mode """

@pytest.fixture()
def setup(browser, headless):
    logger = LogGeneration.customLogger()
    global driver
    if browser is None and headless is None:
        driver = webdriver.Chrome()
    elif browser is not None and headless is None:
        driver = get_driver(browser)
    elif browser is not None or headless is not None:
        driver = browser_options(browser, headless)
    logger.info("driver launched successfully")
    driver.get(Config.URL)
    driver.maximize_window()
    sleep(2)
    # driver.delete_all_cookies()
    driver.implicitly_wait(Config.MIN_TIMEOUT)
    yield driver
    driver.quit()
    logger.info("window closed successfully")



""" Code to take Screenshot """

def _capture_screenshot():
    return driver.get_screenshot_as_base64()



""" Code to attach Screenshot to the html Report generated """

import pytest
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url(Config.URL))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra


""" Code to Display title for Report using Pytest Hooks """

def pytest_html_report_title(report):
	report.title = "Nop Commerce Admin Application Detailed Report"


""" Code to Display basic informations like Project Name, Module Name and Automation Engineer Name on Report using Pytest Hooks """

def pytest_configure(config):
    config._metadata["Project Name"] = "nopCommerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Framework_Developer"] = "Kiran"

""" Code to Remove extra content on html report """

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



""" Code to Pass Browser Name/Value as argument from CLI/HOOKS and Return Nmae/Value to Setup Method """

def pytest_addoption(parser):       ## This Will Get The Value From CLI/HOOKS
    parser.addoption("--browser")
    parser.addoption("--headless")

@pytest.fixture()
def browser(request):       ## This Will Return The Browser Value/Name To Setup Method
    return request.config.getoption("--browser")

@pytest.fixture()
def headless(request):      ## This Will Return The headless Value/Name To Setup Method
    return request.config.getoption("--headless")



""" To Eliminate some extra details """

# # from datetime import datetime
# # from py.xml import html
# # import pytest
# #
# # def pytest_html_results_table_header(cells):
# #     cells.insert(2, html.th("Description"))
# #     cells.insert(1, html.th("Time", class_="sortable time", col="time"))
# #     cells.pop()
# #
# #
# # def pytest_html_results_table_row(report, cells):
# #     cells.insert(2, html.td(report.description))
# #     cells.insert(1, html.td(datetime.utcnow(), class_="col-time"))
# #     cells.pop()
# #
# #
# # @pytest.hookimpl(hookwrapper=True)
# # def pytest_runtest_makereport(item, call):
# #     outcome = yield
# #     report = outcome.get_result()
# #     report.description = str(item.function.__doc__)


## pytest -v -s testCases/test_01_login.py --browser firefox --headless yes    --  To Run Code in Headless Mode