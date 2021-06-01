from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Timesheet.Pages.loginPage import LoginPage
from Timesheet.Pages.homePage import HomePage
from Timesheet.Pages.timesheetPage import TimesheetPage
import HtmlTestRunner

class TimesheetTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_timesheet(self):
        driver = self.driver
        driver.get("https://rev2.force.com/revature/s/login/?ec=302&startURL=%2Frevature%2Fs%2Ftimesheet")

        login = LoginPage(driver)
        login.enter_username("Sample Username")
        login.enter_password("Sample Password")
        time.sleep(2)
        login.click_login()

        driver = self.driver
        home = HomePage(driver)
        home.click_current_timesheet()
        time.sleep(2)

        timesheet = TimesheetPage(driver)
        timesheet.enter_monday("8")
        timesheet.enter_tuesday("8")
        timesheet.enter_wednesday("8")
        timesheet.enter_thursday("8")
        timesheet.enter_friday("8")
        print(f'Here is the Submit button: {timesheet.submit_text()}')
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/18587/OneDrive/Desktop/Git/TimeSheet/Timesheet/Report"))