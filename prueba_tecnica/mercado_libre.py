from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MercadoLibrePage(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'http://mercadolibre.com'
        self.search_class_name = 'nav-search-input'
        self.new_ones_link_xpath = '//a[@aria-label="Nuevo"]'
        self.guayas_xpath = '//a[@aria-label="Guayas"]'

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, 'EC')
            )
        )
        return True

    @property
    def are_products_loaded(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//span[@class="price-tag-fraction"]')
            )
        )
        return True


    def open(self):
        self._driver.maximize_window()
        self._driver.get(self._url)

    def select_country(self, country):
        self._driver.find_element_by_id(country).click()

    def type_search_submit(self, keyword):
        input_field = self._driver.find_element_by_class_name(
            self.search_class_name)
        input_field.send_keys(keyword)
        input_field.submit()

    def filter_new_ones(self):
        self._driver.find_element_by_xpath(self.new_ones_link_xpath).click()

    def filter_by_city(self):
        self._driver.find_element_by_xpath(self.guayas_xpath).click()

    def click_filter(self):
        self._driver.find_element_by_css_selector(
            '#root-app > div > div > section > div.ui-search-view-options__container > div > div > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > button').click()

    def select_higher_to_lower(self):
        self._driver.find_element_by_css_selector(
            '#root-app > div > div > section > div.ui-search-view-options__container > div > div > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > div > ul > li:nth-child(3) > a').click()

    def filter_higher_lower(self):
        self.click_filter()
        self.select_higher_to_lower()

    def get_product_names(self):
        product_names =  self._driver.find_elements_by_xpath('//h2[@class="ui-search-item__title"]')
        product_names =  map(lambda product_name: product_name.text, product_names)
        return product_names

    def get_product_prices(self):
        product_prices = self._driver.find_elements_by_xpath('//span[@class="price-tag-fraction"]')
        product_prices =  map(lambda product_name: product_name.text, product_prices)
        return product_prices
    
    def get_products_info(self):
        return list(zip(self.get_product_names(), self.get_product_prices()))
