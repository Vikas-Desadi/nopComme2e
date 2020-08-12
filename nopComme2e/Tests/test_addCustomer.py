import random
import string

import pytest

from pageObjects.loginpage import login
from pageObjects.addCustomerPage import AddCustomers
from Utilities.readProperties import readConfig
from Utilities.customLogger import logGen

class Test_003_AddCustomer:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUserName()
    password = readConfig.getPassword()
    logger = logGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.vikas
    def test_addCustomer(self, setup):
        self.logger.info("*************** Test_003 Strted ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()
        self.logger.info("************ Login Succesful **************")

        self.logger.info("************ Add customer start **************")
        self.addcust = AddCustomers(self.driver)
        self.addcust.clickonCustomersMenu()
        self.addcust.clickonCustomersMenuItem()

        self.addcust.clickOnAddnew()
        self.logger.info("***************** Providing cust info***************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Vikas")
        self.addcust.setLastName("Desadi")
        self.addcust.setGender("Male")
        self.addcust.setDob("03/29/1990")  #M/D/YYYY
        self.addcust.setCompanyName("Coolsoft")
        self.addcust.setCustomerRoles("Registered")
        self.addcust.setMnagerOfVendor("Vendor 2")
        self.addcust.setAdmonComment("This is for testing")
        self.addcust.clickonSave()

        self.logger.info("************ Saving the info *************")
        self.msg= self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("********** Add cusomer Passed *********")

        else:
            self.driver.save_screenshot(".//Sceeenshots//"+"test_addcustomer_src.png")
            self.logger.info("********** Add cusomer failed *********")
            assert True == False

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
