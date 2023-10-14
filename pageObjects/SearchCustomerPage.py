from selenium.webdriver.common.by import By
from utilities.seleniumLibrary import SeleniumCore

class SearchCustomer:

    """ Objects of respective page """
    textbox_email_id = "SearchEmail"
    textbox_fname_id = "SearchFirstName"
    textbox_lname_id = "SearchLastName"
    button_search_id = "(//i[@class='fas fa-search'])[2]"
    table_xpath = "//table[@id='customers-grid']"
    table_row_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_column_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver
        self.selenium_core = SeleniumCore(self.driver)

    def setSearchEmail(self,search_email):
        self.selenium_core.clear_text_field(By.ID, self.textbox_email_id)
        self.selenium_core.send_keys(By.ID, self.textbox_email_id, search_email)

    def setSearchFirstName(self,search_fname):
        self.selenium_core.clear_text_field(By.ID, self.textbox_fname_id)
        self.selenium_core.send_keys(By.ID, self.textbox_fname_id, search_fname)

    def setSearchLastName(self,search_lname):
        self.selenium_core.clear_text_field(By.ID, self.textbox_lname_id)
        self.selenium_core.send_keys(By.ID, self.textbox_lname_id, search_lname)

    def clickOnSearch(self):
        self.selenium_core.click_element(By.XPATH, self.button_search_id)

    def getNoOfRows(self):
        row_ele = self.selenium_core.get_elements(By.XPATH, self.table_row_xpath)
        return len(row_ele)

    def getNoOfColumns(self):
        col_ele = self.selenium_core.get_elements(By.XPATH, self.table_column_xpath)
        return len(col_ele)

    def searchCustomerByEmail(self,search_email):
        flag = False
        for row in range(1, self.getNoOfRows()+1):
            email_id = self.selenium_core.get_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(row)+"]/td[2]").text
            if email_id == search_email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,search_name):
        flag = False
        for row in range(1, self.getNoOfRows() + 1):
            name = self.selenium_core.get_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(row)+"]/td[3]").text
            if name == search_name:
                flag = True
                break
        return flag