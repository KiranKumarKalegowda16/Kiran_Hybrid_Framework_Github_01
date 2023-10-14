from configurations.config import Config
from pageObjects import AddCustomerPage, LoginPage, SearchCustomerPage
from utilities.customLogger import LogGeneration
from utilities.excelLibrary import read_test_data
import pytest
from utilities.seleniumLibrary import SeleniumCore
from selenium.webdriver.common.by import By
from utilities.randomGenerator import Generic_Utilities
from time import sleep


class Test_004_SearchCustomersByName:

    logger = LogGeneration.customLogger()
    header, data = read_test_data("new_sheet_one", "nop_demo_login_page_data", Config.excel_file_path)
    header1, data1 = read_test_data("new_sheet_one", "nop_demo_search_customer_by_name", Config.excel_file_path)


    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.parametrize(header1, data1)
    @pytest.mark.parametrize(header, data)
    def test_search_customers(self, setup, username, password, login_page_expected_title, search_name, search_fname, search_lname):
        self.driver = setup
        self.login_pom_page = LoginPage.Login(self.driver)
        self.addCustomer_pom_page = AddCustomerPage.AddCustomer(self.driver)
        self.searchCustomer_pom_page = SearchCustomerPage.SearchCustomer(self.driver)

        self.selenium_core = SeleniumCore(self.driver)

        self.login_pom_page.setUserName(username)
        self.logger.info("***********  entered_login_user_name  ***********")
        self.login_pom_page.setPassWord(password)
        self.logger.info("***********  entered_login_password  ***********")
        self.login_pom_page.clickLogin()
        self.logger.info("***********  clicked_on_login_button  ***********")
        self.addCustomer_pom_page.clickOnCustomersMenu()
        self.logger.info("***********  Clicked_on_customers_main_menu  ***********")
        self.addCustomer_pom_page.clickOnCustomersSubMenu()
        self.logger.info("***********  Clicked_on_customers_sub_main_menu  ***********")
        # self.addCustomer_pom_page.clickOnSearchCustomers()
        # self.logger.info("***********  Clicked_on_search_icon_on_sub_main_menu  ***********")
        # sleep(10)
        self.searchCustomer_pom_page.setSearchFirstName(search_fname)
        self.logger.info("***********  Searching_customer_by_entering_first_name  ***********")
        self.searchCustomer_pom_page.setSearchLastName(search_lname)
        self.logger.info("***********  Searching_customer_by_entering_last_name  ***********")
        self.searchCustomer_pom_page.clickOnSearch()
        self.logger.info("***********  Clicked_on_search_button_after_entering_email_id  ***********")
        sleep(2)
        self.logger.info("***********  Searching_for_the_customer_name_in_table  ***********")
        search_name_status = self.searchCustomer_pom_page.searchCustomerByName(search_name)
        assert True == search_name_status
        self.logger.info("***********  Test_003_SearchCustomersByName_Finished  ***********")

