from unittest import TestCase, main
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Assertions(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")

    def test_search_text_field(self):
       self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_options(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present(self, how, what):
        """Utility function that will indicate if an element(Selector) is present

        :param how: Indicate the way the selector is going to be found (By.NAME, By.ID, ect)
        :type how: By
        :param what: The value of the how attrribute, the selector has
        :type what: str
        :return: true if exist, false if not
        :rtype: boolean
        """

        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as nsee:
            print("The element does not exist :", nsee)
            return False
        return True


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="reports_assertions", report_name="assertions"))
