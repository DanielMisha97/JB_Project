import unittest

from Home_Practice.JB_project.pages.productPageN import productPageN
from Home_Practice.JB_project.tests.baseSeleniumN import baseSelenium3
from Home_Practice.JB_project.tests.globalsN import url


class test_starbucks(unittest.TestCase):


    def test_coffe(self):

        base = baseSelenium3()

        driver = base.selenium_start(url)
        product_page = productPageN(driver)
        product_page.accept_cookies()
        product_page.coffeMenu()
        product_page.hotCoffe()
        product_page.Cappucino()
        product_page.menu2()
        product_page.lunch()







        base.selenium_end(driver)