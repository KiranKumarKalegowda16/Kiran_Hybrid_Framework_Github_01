from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from configurations.config import Config


""" Wait (3 Conditions):
 1. Check if the element is loaded in the DOM
 2. Check if the element is visible on the webpage.
 3. Check if the element is enabled or not? """

# class _visibility_of_element_located(visibility_of_element_located):
#     def __init__(self, locator):
#         super().__init__(locator)
#
#     """over-riding __call__ method of parent class"""
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         """Checking if __call__ has returned a WebElement? , Extra functionality that we are adding in child class
#         checking for enablement of the element"""
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         return result


def wait(func):
    def wrapper(*args, **kwargs):  # args = (self, ("link text", "Register"))
        instance = args[0]
        locator = args[1:3]  # get the inner tuple
        """ Performing Wait (Checking for 2 Conditions) """
        wait = WebDriverWait(instance.driver,Config.MAX_TIMEOUT)
        """ Performing Wait (Checking for 3 Conditions) """
        # v = _visibility_of_element_located(locator)
        v = visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)  # original func is executed (click_element, enter_text,select_item, select_items)
    return wrapper