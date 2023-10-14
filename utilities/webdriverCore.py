from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

""" Here get_driver() function is used to execute test scripts in requested/choosen browser 
and browser_options() function is used to execute scripts in headless mode"""

def get_driver(browser):
    if browser.lower() == "firefox":
        driver = Firefox()
    elif browser.lower() == "edge":
        driver = Edge()
    elif browser.lower() == "chrome":
        driver = Chrome()
    return driver

def browser_options(browser, headless):
    if headless.lower() == "yes":
        if browser.lower() == "firefox":
            firefox_option = FirefoxOptions()
            firefox_option.headless = True
            driver = Firefox(options=firefox_option)
        elif browser.lower() == "edge":
            edge_option = EdgeOptions()
            edge_option.add_argument("--headless")
            driver = Edge(options=edge_option)
        elif browser.lower() == "chrome":
            chrome_option = ChromeOptions()
            chrome_option.headless = True
            driver = Chrome(options=chrome_option)
        else:
            chrome_option = ChromeOptions()
            chrome_option.headless = True
            driver = Chrome(options=chrome_option)
    else:
        driver = get_driver(browser)
    return driver


