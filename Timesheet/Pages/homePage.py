from Timesheet.Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.open_current_timesheet_button_xpath = Locators.open_current_timesheet_button_xpath

    def click_current_timesheet(self):
        self.driver.find_element_by_xpath(self.open_current_timesheet_button_xpath).click()
        