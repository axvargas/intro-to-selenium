from unittest import TestCase, main
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

class NavigationTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://google.com")

    def test_broewser_navigation(self):
        # * Get the input search and clear the textfield
        driver = self.driver
        search_input = driver.find_element_by_name('q')

        search_input.clear() #this is a good practice

        # * Search fot 'platzi'
        search_input.send_keys("platzi")
        search_input.submit()
        sleep(3)
        #  * go back
        driver.back()
        sleep(3)
        # * go ahead
        driver.forward()
        sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="reports/automatic_navigation", report_name="test_automatic_navigation", add_timestamp=False))