import pytest

from Utilities.readProperties import readConfig
from Utilities.customLogger import logGen
from pageObjects.loginpage import login
from Utilities import XLUtils

class Test_002_login:
    baseURL = readConfig.getApplicationURL()
    # username = readConfig.getUserName()
    # password = readConfig.getPassword()
    logger = logGen.loggen()

    @pytest.mark.sanity
    def test_loginPage(self, setup):
        self.logger.info("**************** Verifying login test *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        lp = login(self.driver)
        path = ".//TestData/My_data.xlsx"
        rows = XLUtils.getRowCount(path, "Sheet1")
        for r in range(2, rows+1):
            self.username = XLUtils.readData(path, "Sheet1", r, 1)
            self.password = XLUtils.readData(path,"Sheet1", r, 2)
            self.exp = XLUtils.readData(path,"Sheet1", r, 3)
            lst_status = []
            lp.setUserName(self.username)
            lp.setPassword(self.password)
            lp.click_login()
            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("**************** login test passed *********")
                    lp.click_logout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":

                    self.logger.error("**************** login test user2 failed *********")
                    lst_status.append("Fail")


            elif act_title != "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("**************** login user 3 failed test test passed *********")


                    lst_status.append("Fail")
                elif self.exp=="Fail":

                    self.logger.error("**************** login user 4 failed test pass *********")
                    lst_status.append("Pass")


        if "Pass" not in lst_status:
            self.logger.error("************* login test ddt is passed ***************")
            self.driver.close()
            assert True

        else:
            self.logger.error("************* login test ddt is failed ***************")
            self.driver.close()
            assert False

        self.logger.error("************* login test ddt passes ***************")
        self.logger.error("************* completed TC_002 ***************")
