import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilitize.utils import Utilz
from base.base_driver import BaseDriver
from page.search_results_page import SearchResult
import logging


class LaunchPage(BaseDriver):
    log = Utilz.custome_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    DEPART_FROM = "BE_flight_origin_city"
    DEPART_TO = "BE_flight_arrival_city"
    DEPART_TO_LIST = "//div[@class='ac_airport']/p"
    SELECT_DATA = "flight_origin_date"
    ONE_DATA = "//tbody[@class='BE_flight_origin_date']//td"
    ALL_DATA_LIST = "//tbody[@class='BE_flight_origin_date']//td"
    SEARCH_BUTTON = "BE_flight_flsearch_btn"

    def get_depart_from_field(self):
        return self.wait_element_to_be_clickable(By.ID, self.DEPART_FROM)

    def get_depart_to_field(self):
        return self.wait_element_to_be_clickable(By.ID, self.DEPART_TO)

    def get_list_of_depart_to(self):
        return self.wait_of_presents_of_all_elements(By.XPATH, self.DEPART_TO_LIST)

    def get_depart_date(self):
        return self.wait_element_to_be_clickable(By.NAME, self.SELECT_DATA)

    def get_one_date(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.ONE_DATA)

    def get_search_button(self):
        return self.wait_element_to_be_clickable(By.ID, self.SEARCH_BUTTON)

    def enter_depart_from_location(self, depart_from):
        self.get_depart_from_field().click()
        self.log.info("Clicked on location from")
        time.sleep(2)
        self.get_depart_from_field().send_keys(depart_from)
        time.sleep(2)
        self.get_depart_from_field().send_keys(Keys.ENTER)

    def enter_depart_to_location(self, depart_to, city_from_list):
        self.get_depart_to_field().click()
        self.log.info("Clicked on location to")
        time.sleep(2)
        self.get_depart_to_field().send_keys(depart_to)
        time.sleep(2)
        results_depart = self.get_list_of_depart_to()
        for result in results_depart:
            if city_from_list in result.text:
                result.click()
                break

    def enter_date_depart(self, value):
        self.get_depart_date().click()
        self.log.info("Pick up the date")
        time.sleep(2)
        all_elements = self.get_one_date().find_elements(By.XPATH, self.ALL_DATA_LIST)
        for date in all_elements:
            if date.get_attribute("data-date") == value:
                date.click()
                break

    def click_search_button(self):
        self.get_search_button().click()

    def search_flights(self, depart_from, depart_to, city_from_list, value):
        self.enter_depart_from_location(depart_from)
        self.enter_depart_to_location(depart_to, city_from_list)
        self.enter_date_depart(value)
        self.click_search_button()
        search_result = SearchResult(self.driver)
        return search_result
