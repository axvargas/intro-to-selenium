from unittest import TestCase, main
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

class ExplicitWaitTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")

    def test_account_link(self):
        WebDriverWait(self.driver, 20).until(lambda s : s.find_element_by_id('select-language').get_attribute('length') == '3')

        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "ACCOUNT")))
        account.click()

    def test_create_new_customer(self):
        # self.driver.find_element_by_link_text('ACCOUNT')
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "My Account")))
        my_account.click()

        create_account_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_btn.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))


    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="reports/waits", report_name="test_waits", add_timestamp=False))