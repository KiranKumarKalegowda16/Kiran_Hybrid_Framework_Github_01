from selenium.webdriver.common.by import By
from utilities.seleniumLibrary import SeleniumCore


class AddCustomer:

    """ Objects of respective page """
    link_customers_mainmenu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customers_submenu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    button_addNew_xpath = "//a[@class='btn btn-primary']"
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_firstname_id = "FirstName"
    textbox_lastname_id = "LastName"
    radiobutton_gender_male_xpath = "//div[@class='form-check']/child::input[@id='Gender_Male']"
    radiobutton_gender_female_xpath = "//div[@class='form-check']/child::input[@id='Gender_Female']"
    dropdown_customerRole_xpath = "//select[@id='SelectedCustomerRoleIds' and @name='SelectedCustomerRoleIds']"
    button_save_xpath = "//button[@name ='save' and @class='btn btn-primary']"
    dd_cus_role_set_xpath = "//div[@class='input-group-append input-group-required']"
    link_search_customers_xpath = "//button[@class='btn btn-primary btn-search' and @id='search-customers']"

    def __init__(self,driver):
        self.driver = driver
        self.selenium_core = SeleniumCore(self.driver)

    def clickOnCustomersMenu(self):
        self.selenium_core.click_element(By.XPATH, self.link_customers_mainmenu_xpath)

    def clickOnCustomersSubMenu(self):
        self.selenium_core.click_element(By.XPATH, self.link_customers_submenu_xpath)

    def clickOnSearchCustomers(self):
        self.selenium_core.click_element(By.XPATH, self.link_search_customers_xpath)

    def clickOnAddNew(self):
        self.selenium_core.click_element(By.XPATH, self.button_addNew_xpath)

    def setEmail(self, email):
        self.selenium_core.clear_text_field(By.ID, self.textbox_email_id)
        self.selenium_core.send_keys(By.ID, self.textbox_email_id, email)

    def setPassword(self, password):
        self.selenium_core.clear_text_field(By.ID, self.textbox_password_id)
        self.selenium_core.send_keys(By.ID, self.textbox_password_id, password)

    def setFirstName(self, firstname):
        self.selenium_core.clear_text_field(By.ID, self.textbox_password_id)
        self.selenium_core.send_keys(By.ID, self.textbox_password_id, firstname)

    def setLastName(self, lastname):
        self.selenium_core.clear_text_field(By.ID, self.textbox_password_id)
        self.selenium_core.send_keys(By.ID, self.textbox_password_id, lastname)

    def clickOnMaleGenderRadioButton(self):
        self.selenium_core.click_element(By.XPATH, self.radiobutton_gender_male_xpath)

    def clickOnFemaleGenderRadioButton(self):
        self.selenium_core.click_element(By.XPATH, self.radiobutton_gender_female_xpath)

    def clickOnDropdownCustomerRoleSelect(self):
        self.selenium_core.click_element(By.XPATH, self.dd_cus_role_set_xpath)

    def selectCustomerRolesDropdown(self,itemtext):
        self.selenium_core.select_option_by_text(By.XPATH, self.dropdown_customerRole_xpath,itemtext)

    def clickOnSaveButton(self):
        self.selenium_core.click_element(By.XPATH, self.button_save_xpath)
