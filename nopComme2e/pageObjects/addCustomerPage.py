import time

from selenium.webdriver.support.select import Select


class AddCustomers:
    #Add customers page
    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_menuitem_Xpath = "//li[4]/ul/li[1]/a/span"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors']"
    drpmgrOFVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickonCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()
        time.sleep(3)

    def clickonCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_Xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem= self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem= self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)

        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)

        elif role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(1)
        #self.listitem.click();   This is not working so use below
        self.driver.execute_script("arguments[0];", self.listitem)

    def setMnagerOfVendor(self,value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOFVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,Compname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(Compname)

    def setAdmonComment(self,text):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(text)

    def clickonSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

























