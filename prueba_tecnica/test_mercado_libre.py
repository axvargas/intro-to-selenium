from unittest import TestCase, main
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from mercado_libre import MercadoLibrePage

class MercadoLibreTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        cls.driver.find_element_by_css_selector

    def test_mercado(self):
        mercado = MercadoLibrePage(self.driver)
        mercado.open()
        self.assertTrue(mercado.is_loaded)
        mercado.select_country("EC")
        mercado.type_search_submit("Play Station 4")
        mercado.filter_new_ones()
        mercado.filter_by_city()
        mercado.filter_higher_lower()
        self.assertTrue(mercado.are_products_loaded)
        products = mercado.get_products_info()

        for product in products:
            print(f'Product: {product[0]}-----> price: {product[1]}')

        expected_no_results = 50
        self.assertEqual(expected_no_results, len(products))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="mercado_libre", report_name="test_mercado_libre"))