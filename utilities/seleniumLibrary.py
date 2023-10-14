from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.waitDecorator import wait
import re


class SeleniumCore:

    """ All selenium methods are stored in SeleniumCore class which is called from respective pom pages
    and all the methods are decorated with wait decorator """

    def __init__(self, driver):
        self.driver = driver

    @wait
    def get_element(self, by_type, locator):
        return self.driver.find_element(by_type, locator)

    @wait
    def get_elements(self, by_type, locator):
        return self.driver.find_elements(by_type, locator)

    @wait
    def send_keys(self, by_type, locator, input_value):
        self.get_element(by_type, locator).send_keys(input_value)

    @wait
    def get_text(self, by_type, locator):
        web_element_text = self.get_element(by_type, locator).text
        return web_element_text

    @wait
    def get_text_from_elements(self, by_type, locator):
        web_elements = self.get_elements(by_type, locator)
        return [element.text for element in web_elements]

    @wait
    def clear_text_field(self, by_type, locator):
        self.get_element(by_type, locator).clear()

    @wait
    def click_element(self, by_type, locator):
        self.get_element(by_type, locator).click()

    @wait
    def js_click_element(self, by_type, locator):
        self.driver.execute_script("arguments[0].click", self.get_element(by_type, locator))

    @wait
    def scroll_to_element(self, by_type, locator):
        self.driver.execute_script("arguments[0].scrollIntoView", self.get_element(by_type, locator))

    @wait
    def scroll_to_bottom_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_till_element_visible(self, by_type, locator, duration=10):
        WebDriverWait(self.driver, duration).until(EC.visibility_of_element_located((by_type, locator)))

    def wait_till_element_invisible(self, by_type, locator, duration=10):
        WebDriverWait(self.driver, duration).until(EC.invisibility_of_element_located((by_type, locator)))

    def wait_till_element_clickable(self, by_type, locator, duration=20):
        WebDriverWait(self.driver, duration).until(EC.element_to_be_clickable((by_type, locator)))

    def wait_till_element_present(self, by_type, locator, duration=10):
        WebDriverWait(self.driver, duration).until(EC.presence_of_element_located((by_type, locator)))

    def wait_till_elements_present(self, by_type, locator, duration=10):
        WebDriverWait(self.driver, duration).until(EC.presence_of_all_elements_located((by_type, locator)))

    def wait_till_element_not_present(self, by_type, locator, duration=20):
        WebDriverWait(self.driver, duration).until(EC.invisibility_of_element((by_type, locator)))

    def wait_till_text_present_in_element(self, by_type, locator, text, duration=20):
        WebDriverWait(self.driver, duration).until(EC.text_to_be_present_in_element((by_type, locator), text))

    def wait_till_title_is(self, title="", duration=10):
        WebDriverWait(self.driver, duration).until(EC.title_is(title))

    def wait_till_title_contains(self, text="", duration=10):
        WebDriverWait(self.driver, duration).until(EC.title_contains(text))

    @wait
    def select_option_by_text(self, by_type, locator, text):
        dropdown_element = Select(self.get_element(by_type, locator))
        dropdown_element.select_by_visible_text(text)
        del dropdown_element

    @wait
    def select_option_by_value(self, by_type, locator, value):
        dropdown_element = Select(self.get_element(by_type, locator))
        dropdown_element.select_by_value(value)
        del dropdown_element

    @wait
    def select_option_by_index(self, by_type, locator, index):
        dropdown_element = Select(self.get_element(by_type, locator))
        dropdown_element.select_by_index(index)
        del dropdown_element

    @wait
    def first_selected_option(self, by_type, locator):
        dropdown_element = Select(self.get_element(by_type, locator))
        selected_option = dropdown_element.first_selected_option
        return selected_option.text

    @wait
    def deselect_option_by_text(self, by_type, locator, text):
        dropdown_element = Select(self.get_element(by_type, locator))
        dropdown_element.deselect_by_visible_text(text)
        del dropdown_element

    @wait
    def deselect_option_by_value(self, by_type, locator, value):
        dropdown_element = Select(self.get_element(by_type, locator))
        dropdown_element.deselect_by_value(value)
        del dropdown_element

    @wait
    def deselect_option_by_index(self, by_type, locator, index):
        dropdown_element = Select(self.get_element(by_type, locator))
        dropdown_element.deselect_by_index(index)
        del dropdown_element

    @wait
    def deselect_all_option(self, by_type, locator):
        dropdown_element = Select(self.get_element(by_type, locator))
        dropdown_element.deselect_all()
        del dropdown_element

    @wait
    def get_all_options(self, by_type, locator):
        dropdown_element = Select(self.get_element(by_type, locator))
        all_options = dropdown_element.options
        return [item.text for item in all_options]

    @wait
    def mouse_over_to_element(self, by_type, locator):
        ActionChains(self.driver).move_to_element(self.get_element(by_type, locator)).perform()

    @wait
    def double_click_on_element(self, by_type, locator):
        ActionChains(self.driver).double_click(self.get_element(by_type, locator)).perform()

    @wait
    def drag_and_drop_element(self, source, destination):
        ActionChains(self.driver).drag_and_drop(source, destination).perform()

    @wait
    def get_hex_color_of_element(self, by_type, locator, css_property):
        res = self.get_element(by_type, locator).value_of_css_property(css_property)
        var = re.findall(r"\d+", res)
        r, g, b, *rest = [int(i) for i in var]
        return self.rgb_to_hex((r, g, b))

    @wait
    def rgb_to_hex(self, rgb):
        return '%02x%02x%02x' % rgb

    @wait
    def get_color_property_of_an_element(self, by_type, locator, css_property):
        return self.get_element(by_type, locator).value_of_css_property(css_property)









