import unittest

from Project1.pages.productPage import productPage3
from Project1.tests.baseSelenium3 import baseSelenium
from Project1.tests.globals3 import url_newegg


class test_price_text(unittest.TestCase):

    def test_first_price_text(self):
        base = baseSelenium()

        driver = base.selenium_start(url_newegg)
        product_page = productPage3(driver)



        product_page.regionChoice()
        product_page.searchBar()
        product_page.get_product_price()
        product_page.add_product()
        product_page.free_shipping()
        product_page.headset_color()
        base.selenium_end(driver)


