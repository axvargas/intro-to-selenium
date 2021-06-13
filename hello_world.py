from unittest import TestCase, main
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver


class HelloWorld(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(30)

    def test_hello_world(self):
        driver = self.driver
        driver.get("https://www.platzi.com")

    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get("https://wikipedia.org")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(output="reports/report_hello", report_name="hello_world_report", add_timestamp=False))

