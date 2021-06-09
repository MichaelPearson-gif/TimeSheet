from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Timesheet.Pages.loginPage import LoginPage
from Timesheet.Pages.homePage import HomePage
from Timesheet.Pages.timesheetPage import TimesheetPage
from Timesheet.utils import utils
import HtmlTestRunner

@pytest.mark.usefixtures("test_setup")
class TimesheetTest(unittest.TestCase):

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        time.sleep(2)
        login.click_login()
        home = HomePage(driver)
        home.click_current_timesheet()
        time.sleep(2)


    # def test_home(self):
    #     driver = self.driver
    #     home = HomePage(driver)
    #     time.sleep(2)
    #     home.click_current_timesheet()
    #     time.sleep(2)


    def test_timesheet(self):
        driver = self.driver
        timesheet = TimesheetPage(driver)
        # timesheet.enter_monday("8")
        # time.sleep(5)
        # timesheet.enter_tuesday("8")
        # time.sleep(5)
        # timesheet.enter_wednesday("8")
        # time.sleep(5)
        # timesheet.enter_thursday("8")
        # time.sleep(5)
        # timesheet.enter_friday("8")
        # time.sleep(5)
        # timesheet.submit_text()
        x = timesheet.total_hours_text()
        assert x == "Total Hours"
        time.sleep(2)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/18587/OneDrive/Desktop/Git/TimeSheet/Timesheet/Report"))