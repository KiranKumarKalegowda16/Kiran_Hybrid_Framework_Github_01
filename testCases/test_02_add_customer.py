from configurations.config import Config
from pageObjects import AddCustomerPage,LoginPage
from utilities.customLogger import LogGeneration
from utilities.excelLibrary import read_test_data
import pytest
from utilities.seleniumLibrary import SeleniumCore
from selenium.webdriver.common.by import By
from utilities.randomGenerator import Generic_Utilities
from time import sleep


class Test_002_AddCustomers:

    logger = LogGeneration.customLogger()
    header, data = read_test_data("new_sheet_one", "nop_demo_login_page_data", Config.excel_file_path)
    header1, data1 = read_test_data("new_sheet_one","nop_demo_add_new_customers_data",Config.excel_file_path)
    link_allContents_xpath = "//body[@class='sidebar-mini layout-fixed control-sidebar-slide-open']"
    random_email_id = Generic_Utilities.random_genrator()

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.parametrize(header, data)
    @pytest.mark.parametrize(header1, data1)
    def test_add_customers(self,setup,cust_email_id,cust_password,cust_firstname,cust_lastname,cust_itemtext,username,password,login_page_expected_title):
        self.driver = setup
        self.login_pom_page = LoginPage.Login(self.driver)
        self.addCustomer_pom_page = AddCustomerPage.AddCustomer(self.driver)
        self.selenium_core = SeleniumCore(self.driver)
        # print(username, password, login_page_expected_title)
        # print(cust_email_id, cust_password, cust_firstname, cust_lastname, cust_itemtext)

        self.login_pom_page.setUserName(username)
        self.login_pom_page.setPassWord(password)
        self.login_pom_page.clickLogin()
        self.logger.info("***********  clicked on login button  ***********")
        login_page_actual_title = self.driver.title
        self.logger.info(login_page_actual_title)
        self.logger.info("***********  getting title of login page  ***********")
        # print(login_page_actual_title)
        # print(self.login_page_expected_title)
        self.logger.info("***********  validation started for actual and expected  ***********")
        if login_page_expected_title == login_page_actual_title:
            self.logger.info("***********  Login_Test_Is_Passed  ***********")
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login_page.png")
            self.logger.error("***********  Login_Test_Is_Failed  ***********")
            assert False

        self.addCustomer_pom_page.clickOnCustomersMenu()
        self.logger.info("***********  Clicked_on_customers_main_menu  ***********")
        self.addCustomer_pom_page.clickOnCustomersSubMenu()
        self.logger.info("***********  Clicked_on_customers_sub_main_menu  ***********")
        self.addCustomer_pom_page.clickOnAddNew()
        self.logger.info("***********  Clicked_on_add_new_button  ***********")
        self.addCustomer_pom_page.setEmail(self.random_email_id + "@gmail.com")
        # sleep(5)
        self.logger.info("***********  Entered_email_address_to_Create_new_customer  ***********")
        self.addCustomer_pom_page.setPassword(cust_password)
        self.logger.info("***********  Entered_password_to_Create_new_customer  ***********")
        self.addCustomer_pom_page.setFirstName(cust_firstname)
        self.logger.info("***********  Entered_firstname_to_Create_new_customer  ***********")
        self.addCustomer_pom_page.setLastName(cust_lastname)
        self.logger.info("***********  Entered_lastname_to_Create_new_customer  ***********")
        self.addCustomer_pom_page.clickOnMaleGenderRadioButton()
        self.logger.info("***********  Selected_gender_as_male_to_Create_new_customer  ***********")
        # self.addCustomer_pom_page.clickOnDropdownCustomerRoleSelect()
        # self.logger.info("***********  Selected_customer_role_dropdown  ***********")
        # self.addCustomer_pom_page.selectCustomerRolesDropdown(cust_itemtext)
        # self.logger.info("***********  Selected_customer_role_as_specified_to_Create_new_customer  ***********")
        self.addCustomer_pom_page.clickOnSaveButton()
        self.logger.info("***********  Clicked_on_save_button_to_Create_a_new_customer  ***********")
        self.web_ele = self.selenium_core.get_text(By.XPATH, Test_002_AddCustomers.link_allContents_xpath)
        # print(type(self.web_ele))
        # print(self.web_ele)
        if "The new customer has been added successfully." in self.web_ele:
            self.logger.info("***********  Add_customer_test_is_passed  ***********")
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login_page.png")
            self.logger.info("***********  Add_customer_test_is_failed  ***********")
            assert False




