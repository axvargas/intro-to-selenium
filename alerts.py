from unittest import TestCase, main
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

class CompareProducts(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")

    def test_compare_products_removal_alert(self):
        # * Get the input search and clear the textfield
        driver = self.driver
        search_input = driver.find_element_by_id('search')

        search_input.clear() #this is a good practice

        # * Search fot the 'tee'
        search_input.send_keys("tee")
        search_input.submit()

        #  * click on compare on two products
        driver.find_element_by_class_name('link-compare').click()

        # * check if the clear all link is displayed to click it an activate the alert
        clear_all_link = driver.find_element_by_link_text('Clear All')

        self.assertTrue(clear_all_link.is_displayed())
        clear_all_link.click()

        # * Switch to the alert context
        alert = driver.switch_to_alert()
        alert_text = alert.text

        # * Assert if the alert is the desired one
        self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)

        driver.implicitly_wait(15)
        alert.accept()
        # alert.dismiss()

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="reports/alerts", report_name="test_alerts", add_timestamp=False))