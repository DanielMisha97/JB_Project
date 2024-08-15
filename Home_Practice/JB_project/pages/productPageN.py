import time


from selenium.webdriver.common.by import By



class productPageN():
    def __init__(self,driver):
        self.driver = driver

    def accept_cookies(self):
        button = self.driver.find_element(By.ID, "truste-consent-button")
        button.click()

    def coffeMenu(self):
        menu = self.driver.find_element(By.CSS_SELECTOR, '[href="https://www.starbucks.com/menu"]')
        menu.click()



    def hotCoffe(self):
        hot_coffe = self.driver.find_element(By.LINK_TEXT, "Hot Coffees")
        hot_coffe.click()
        time.sleep(2)

    def Cappucino(self):
        capucino = self.driver.find_element(By.LINK_TEXT, "Cappuccino")
        capucino.click()

        tall_capucino = self.driver.find_element(By.CLASS_NAME, "cursor-pointer")
        tall_capucino.click()
        time.sleep(2)

        button = self.driver.find_element(By.CSS_SELECTOR, "button.sb-button.sb-button--text")
        button.click()

        select_milk = self.driver.find_element(By.CSS_SELECTOR, "select.select__input")
        select_milk.click()

        option_to_select = self.driver.find_element(By.XPATH, "//option[text()='Vanilla Sweet Cream']")
        option_to_select.click()
        selected_option = select_milk.get_attribute("value")
        print(f"Selected value: {selected_option}")

        add_to_order = self.driver.find_element(By.CSS_SELECTOR, "button.sb-frap.sb-frap--centerSVG[data-e2e='add-to-order-button']")
        add_to_order.click()

        assert tall_capucino is not None, "The coffee size is not Tall."
        print("The coffe size is tall")

        selected_option_text = option_to_select.text
        assert selected_option_text == "Vanilla Sweet Cream", f"Expected 'Vanilla Sweet Cream', but got '{selected_option_text}'"
        print("The milk option is correctly set to Vanilla Sweet Cream.")


    def menu2(self):
        menu2 = self.driver.find_element(By.CSS_SELECTOR, "a.sb-globalNav__desktopLink[href='/menu']")
        menu2.click()


    def lunch(self):
        lunch_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/menu/food/lunch"]')
        lunch_link.click()
        product_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/menu/product/574/single"]')
        product_link.click()
        full_nutrition_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-e2e="fullNutritionLink"]')
        full_nutrition_link.click()
        calories_div = self.driver.find_element(By.CSS_SELECTOR, 'div.calories___HqGcu')
        calories_span = calories_div.find_element(By.CSS_SELECTOR, 'span.text-semibold > span:nth-of-type(2)')
        calories_text = calories_span.text
        calories_value = int(calories_text)
        assert calories_value == 500, f"Expected 500 calories, but found {calories_value}."





    # def gift(self):
    #     gift_cards = self.driver.find_element(By.CSS_SELECTOR, "a.sb-globalNav__desktopLink[href='/gift']")
    #     gift_cards.click()
    #     happy_birthday = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/gift/00000328"]')
    #     happy_birthday.click()
    #     gift = self.driver.find_element(By.CSS_SELECTOR, 'select#amount')
    #     gift.click()
    #     hundred_dollars = self.driver.find_element(By.CSS_SELECTOR, 'select#amount > option[value="100"]')
    #     hundred_dollars.click()
    #     input_field = self.driver.find_element(By.CSS_SELECTOR, 'label[for="recipientName1723684997150"] + input')
    #     input_field.click()
    #     input_field.send_keys("daniel")