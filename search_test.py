from unittest import TestCase, main
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver


class Searcher(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get("http://demo-store.seleniumacademy.com")

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self):
        btn = self.driver.find_element_by_class_name("search-button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))

    def test_search_img_promo(self):
        img_promo = self.driver.find_element_by_xpath(
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    def test_search_shopping_cart(self):
        cart_icon = self.driver.find_elements_by_css_selector(
            '#header > div > div.skip-links > div > div > a > span.icon')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="reports/reports_search", report_name="search_test", add_timestamp=False))
