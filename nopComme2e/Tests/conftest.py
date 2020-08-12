from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/pr243589/PycharmProjects/nopComme2e/Drivers/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="/Users/pr243589/PycharmProjects/nopComme2e/Drivers/geckodriver")
    elif browser == "safari":
        driver = webdriver.Safari()
    return driver


def pytest_addoption(parser):  # This will get value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


'''........................Pytest HTML reports.......'''

#It will hook for adding Environment info to HTML Report
# This is an added advantage thats it you can use this or not ur wish
def pytest_configure(config):
    config._metadata['project Name']= 'nop Commerce'
    config._metadata['Module Name']= 'Customers'
    config._metadata['Tester'] = 'Vikas'

#It i s hook for delete/modify Environment info to HTML Report ....
# The below ones will come bydefault so i dont want them in my report so deleting them
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# #to run in parllel based on methods you have -n = 3(methods in class) is max  plugin for this pytest-xdist
# pytest -v -s -n=2 --html=Reports/report.html TestCases/test_login.py --browser chrome
# pytest -v -s -n=2 --html=Reports/report.html TestCases/test_login.py --browser firefox

