from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By


class SearchResult(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    FILTER_FLIGHTS = "//div[@class='filter-heading pr sticky full-width']//label[2]"
    ALL_SPAN_ELEMENT_ONE_STOP = "//span[@class='dotted-borderbtm'][normalize-space()='1 Stop']"

    def get_filter_flights(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.FILTER_FLIGHTS)

    def get_all_element_one_stop(self):
        return self.wait_of_presents_of_all_elements(By.XPATH, self.ALL_SPAN_ELEMENT_ONE_STOP)

    def click_filter_flights(self):
        self.get_filter_flights().click()

