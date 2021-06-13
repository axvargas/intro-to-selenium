from unittest import TestCase, main
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.packages.six import remove_move


class AddRemoveElements(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_name_elements(self):
        driver = self.driver
        checkbox_control = driver.find_element_by_css_selector(
            '#checkbox > input[type=checkbox]')
        checkbox_control.click()

        remove_add_btn = driver.find_element_by_css_selector(
            '#checkbox-example > button')
        remove_add_btn.click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#checkbox-example > button')
            )
        )
        remove_add_btn.click()

        enable_disable_btn = driver.find_element_by_css_selector(
            '#input-example > button')
        enable_disable_btn.click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#input-example > button')
            )
        )

        textfield = driver.find_element_by_css_selector(
            '#input-example > input[type=text]')
        textfield.send_keys("Man de Barro")
        enable_disable_btn.click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#input-example > button')
            )
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="dynamic_controls", report_name="test_dynamic_controls"))
