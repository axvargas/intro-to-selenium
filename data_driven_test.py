from unittest import TestCase, main
import csv
from ddt import ddt, data, unpack
from pyunitreport import HTMLTestRunner
from selenium import webdriver


def get_data(file_name):
    rows = []
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            rows.append(row)
    return rows


@ddt
class SearchDDT(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")

    # @data(('dress', 6), ('music', 5))
    @data(*get_data('testdata.csv'))
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        expected_count = int(expected_count)
        if expected_count > 0:
            products = driver.find_elements_by_xpath(
                '//h2[@class="product-name"]/a')
            self.assertEqual(expected_count, len(products))
            print(f'\n\n\n\nFound {len(products)} products')
            for product in products:
                print(product.text)

        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.',
                             message.text.strip())

            print(f'\n\n\n\nFound 0 products')

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="ddt", report_name="test_ddt"))
