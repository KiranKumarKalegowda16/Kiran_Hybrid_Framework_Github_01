from configurations.config import Config
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGeneration
from utilities.excelLibrary import read_test_data
import pytest


class Test_001_Login:

    # username = "admin@yourstore.com"
    # password = "admin"
    # home_page_expected_title = "Your store. Login"
    # login_page_expected_title = "Dashboard / nopCommerce administration"

    logger = LogGeneration.customLogger()
    header, data = read_test_data("new_sheet_one","nop_demo_home_page_validation",Config.excel_file_path)


    @pytest.mark.sanity
    @pytest.mark.parametrize(header, data)
    def test_home_page_title(self,setup,home_page_expected_title):
        self.logger.info("***********  Test_home_page_title_verifying_001  ***********")
        self.logger.info("***********  Verifying  ***********")
        self.driver = setup
        home_page_actual_title = self.driver.title
        self.logger.info(home_page_actual_title)
        self.logger.info(home_page_expected_title)
        print(home_page_actual_title)
        print(home_page_expected_title)
        if home_page_actual_title == home_page_actual_title:
            self.logger.info("***********  Home_Page_Title_Verified_Sucessfully  ***********")
            assert  True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\"+"test_home_page_title.png")
            self.logger.error("***********  Home_Page_Title_Failed  ***********")
            assert False

    header, data = read_test_data("new_sheet_one","nop_demo_login_page_data",Config.excel_file_path)

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.parametrize(header, data)
    def test_login_page(self,setup,username,password,login_page_expected_title):
        self.logger.info(login_page_expected_title)
        self.logger.info("***********  Test_login_page_title_verifying_001  ***********")
        self.logger.info("***********  Verifying  ***********")
        self.driver = setup
        self.login_pom_page = Login(self.driver)
        self.login_pom_page.setUserName(username)
        self.login_pom_page.setPassWord(password)
        self.login_pom_page.clickLogin()
        self.logger.info("***********  clicked on login button  ***********")
        login_page_actual_title = self.driver.title
        self.logger.info(login_page_actual_title)
        self.logger.info("***********  getting title of login page  ***********")
        self.login_pom_page.clickLogout()
        self.logger.info("***********  clicked on logout page  ***********")
        # print(login_page_actual_title)
        # print(self.login_page_expected_title)
        self.logger.info("***********  validation started for actual and expected  ***********")
        if login_page_expected_title == login_page_actual_title:
            self.logger.info("***********  Login_Test_Is_Passed  ***********")
            assert  True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login_page.png")
            self.logger.error("***********  Login_Test_Is_Failed  ***********")
            assert False
