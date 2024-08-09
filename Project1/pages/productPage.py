
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class productPage3():
    def __init__(self,driver):
        self.driver = driver
        


    def regionChoice(self):
        usa_button = self.driver.find_element(By.CLASS_NAME,"button.button-m.bg-white")
        usa_button.click()

    def searchBar(self):
        search = self.driver.find_element(By.CSS_SELECTOR,"input[title = 'Search Site']")
        search.click()
        search.send_keys("steelseries arctis nova pro wireless")
        search.send_keys(Keys.RETURN)
        time.sleep(2)

    def get_product_price(self):
        price_element = self.driver.find_element(By.CLASS_NAME, "price-current")
        price_strong = price_element.find_element(By.TAG_NAME, "strong").text
        price_sup = price_element.find_element(By.TAG_NAME, "sup").text

        full_price = f"${price_strong}{price_sup}"
        assert  full_price == "$349.99" , ' the price isnt 349.99$'
        print(f"Price found: {full_price}")

    def add_product(self):
        link = self.driver.find_element(By.XPATH,'//a[@href="https://www.newegg.com/steelseries-arctis-nova-pro-wireless-for-xbox-black/p/N82E16826249270"]')
        link.click()


    def free_shipping(self):
        delivery_info = self.driver.find_element(By.CLASS_NAME, 'product-delivery-title')
        free_shipping_text = delivery_info.find_element(By.CLASS_NAME, 'product-price-ship-eligible').text
        location_text = delivery_info.find_elements(By.TAG_NAME, 'span')[1].text
        free_shipping_text = free_shipping_text()
        location_text = location_text()
        assert free_shipping_text == "Free Shipping", f'Expected "Free Shipping", but got "{free_shipping_text}"'
        assert location_text == "from United States", f'Expected "from United States", but got "{location_text}"'

    def headset_color(self):
        color = self.driver.find_element(By.CSS_SELECTOR, 'strong.form-current-value')
        product_color = color.text()
        assert product_color == "Black", f'The product color is not Black, it is {product_color}'
