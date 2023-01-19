import allure
import pytest
import softest
from page.launch_page_yatro import LaunchPage
import time
from utilitize.utils import Utilz
from ddt import ddt, data, unpack, file_data


@ddt()
@pytest.mark.usefixtures("setup")
class TestOne(softest.TestCase):
    log = Utilz.custome_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.l = LaunchPage(self.driver)
        self.ut = Utilz()

    # @data(("New Delhi", "New York", "New York (NYC)", "23/01/2023"), ("New York", "London", "London", "26/01/2023"))
    # @unpack
    @allure.description("This is the first test with screenshort")
    @pytest.mark.ui
    @file_data("/Users/evgen/PycharmProjects/Selenium/testdata/testdata.json")
    def test_search_trip(self, going_from, going_to, auto_going_to, date):
        search_result = self.l.search_flights(going_from, going_to, auto_going_to, date)
        time.sleep(2)
        self.l.page_scroll()
        time.sleep(3)
        search_result.click_filter_flights()
        self.log.info("Select 1 Stop")
        self.ut.assert_item_in_list(search_result.get_all_element_one_stop(), "1 Stop")
