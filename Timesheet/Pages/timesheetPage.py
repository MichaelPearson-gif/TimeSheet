from Timesheet.Locators.locators import Locators

class TimesheetPage():

    def __init__(self, driver):
        self.driver = driver
        self.monday_textbox_id = Locators.monday_textbox_id
        self.tuesday_textbox_id = Locators.tuesday_textbox_id
        self.wednesday_textbox_id = Locators.wednesday_textbox_id
        self.thursday_textbox_id = Locators.thursday_textbox_id
        self.friday_textbox_id = Locators.friday_textbox_id
        self.submit_button_xpath = Locators.submit_button_xpath

    def enter_monday(self, monday):
        self.driver.find_element_by_id(self.monday_textbox_id).clear()
        self.driver.find_element_by_id(self.monday_textbox_id).send_keys(monday)

    def enter_tuesday(self, tuesday):
        self.driver.find_element_by_id(self.tuesday_textbox_id).clear()
        self.driver.find_element_by_id(self.tuesday_textbox_id).send_keys(tuesday)

    def enter_wednesday(self, wednesday):
        self.driver.find_element_by_id(self.wednesday_textbox_id).clear()
        self.driver.find_element_by_id(self.wednesday_textbox_id).send_keys(wednesday)

    def enter_thursday(self, thursday):
        self.driver.find_element_by_id(self.thursday_textbox_id).clear()
        self.driver.find_element_by_id(self.thursday_textbox_id).send_keys(thursday)

    def enter_friday(self, friday):
        self.driver.find_element_by_id(self.friday_textbox_id).clear()
        self.driver.find_element_by_id(self.friday_textbox_id).send_keys(friday)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()