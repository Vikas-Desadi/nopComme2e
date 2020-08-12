import pytest

from pageObjects.loginpage import login
from Utilities.readProperties import readConfig
from Utilities.customLogger import logGen

class Test_001_login:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUserName()
    password = readConfig.getPassword()
    logger = logGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.vikas
    @pytest.mark.regression
    def test_homepageTitle(self, setup):
        self.logger.info("**************** Test_001_login*********")
        self.logger.info("**************** verifying homepage title *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title= self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************** homepage title passed *********")

        else:
            self.driver.save_screenshot(".//Sceeenshots"+"login_error.png")
            self.driver.close()
            self.logger.error("**************** homepage title failed *********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.vikas
    def test_loginPage(self, setup):
        self.logger.info("**************** Verifying login test *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        lp = login(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.click_login()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("**************** login test passed *********")
            assert True
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("**************** login test failed *********")
            assert False

    # pytest - v - s - n = 2 Tests / test_login.py - -browser chrome            #n is for parllel test
