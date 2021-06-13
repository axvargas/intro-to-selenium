from unittest import TestCase, main
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver


class Searcher(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://demo-store.seleniumacademy.com")

    def test_search_tee(self):
        driver = self.driver
        search_text_field = driver.find_element_by_id("search")
        search_text_field.clear()

        search_text_field.send_keys("tee")
        search_text_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_text_field = driver.find_element_by_id("search")
        search_text_field.clear()

        search_text_field.send_keys("salt shaker")
        search_text_field.submit()

        products = driver.find_elements_by_xpath(
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/a')
        self.assertGreaterEqual(len(products), 1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="reports_searcher", report_name="search_test"))
