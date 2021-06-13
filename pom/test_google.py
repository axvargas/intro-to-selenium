from unittest import TestCase, main
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from google_page import GooglePage

class GoogleTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search("Platzi")

        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="google", report_name="test_google"))
