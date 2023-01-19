from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
import logging
import time

class Base:
    # def __init__(self):
    #     self.wd = webdriver.Chrome(ChromeDriverManager().install())

    # def check_name(self):
    #     self.wd.get('https://www.yatra.com/')
    #     text = self.wd.find_element(By.CSS_SELECTOR, ".main-heading").text
    #     print(text)
    #     self.wd.quit()

    def add_param(self, a, b):
        return a + b

pm = Base()
result = pm.add_param(5, 10)
logging.warning(f"return a result {result}")


# @pytest.mark.parametrize('a, b, fin', [(2, 6, 8), (6, 6, 15), (5, 10, 15)])
# def testAdd(a, b, fin):
#     assert a + b == fin
#     logging.warning(f"Something happend {fin}")