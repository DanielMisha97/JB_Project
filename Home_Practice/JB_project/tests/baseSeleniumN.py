from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
class baseSelenium3():


     def selenium_start(self, url):
            print("Test start")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.get(url)

            return driver

     def selenium_end(self, driver):
            driver.close()
            print("Test end")