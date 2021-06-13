from unittest import TestCase, main
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class SelectLanguage(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")

    def test_select_language(self):
        exposed_options = ['English', 'French', 'German']
        active_options = []

        driver = self.driver
        select_language = Select(driver.find_element_by_id('select-language'))

        self.assertEqual(3, len(select_language.options))
        
        # ? Get the language options
        for option in select_language.options:
            active_options.append(option.text)

        # ? Assert if the languages are the exppected ones
        self.assertEqual(exposed_options, active_options)

        # ? Validate that the actual language is English
        self.assertEqual('English', select_language.first_selected_option.text)

        # ? Change language to German
        select_language.select_by_visible_text('German')

        self.assertTrue('store=german' in driver.current_url)

        # * Another way of selecting the language
        # ! It is important to select the Select again
        select_language = Select(driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="reports/select_language", report_name="select_language_test", add_timestamp=False))