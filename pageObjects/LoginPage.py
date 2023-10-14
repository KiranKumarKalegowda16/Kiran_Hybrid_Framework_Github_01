from selenium.webdriver.common.by import By
from utilities.seleniumLibrary import SeleniumCore

class Login:

    """ Objects of respective page """
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[text()='Log in']"
    link_logout_xpath = "//a[text()='Logout']"


    def __init__(self,driver):
        self.driver = driver
        self.selenium_core = SeleniumCore(self.driver)

    def setUserName(self,username):
        self.selenium_core.clear_text_field(By.ID,self.textbox_username_id)
        self.selenium_core.send_keys(By.ID, self.textbox_username_id,username)


    def setPassWord(self, password):
        self.selenium_core.clear_text_field(By.ID, self.textbox_password_id)
        self.selenium_core.send_keys(By.ID, self.textbox_password_id,password)


    def clickLogin(self):
        self.selenium_core.click_element(By.XPATH, self.button_login_xpath)


    def clickLogout(self):
        self.selenium_core.js_click_element(By.XPATH, self.link_logout_xpath)
