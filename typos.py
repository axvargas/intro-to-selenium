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
        driver.find_element_by_link_text('Typos').click()

    def test_name_elements(self):
        driver = self.driver
        flag = True
        tries = 1
        while flag:
            try:
                paragraph_to_check = driver.find_element_by_css_selector(
                    '#content > div > p:nth-child(3)')
                text_to_check = paragraph_to_check.text
                correct_text = "Sometimes you'll see a typo, other times you won't."
                
                self.assertEqual(correct_text, text_to_check)
                flag = False
            except AssertionError as ae:
                print("It failed :(, I 'll try again")
                tries += 1
                driver.refresh()

        print(f'Finished in {tries} tries')

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="typos", report_name="test_typos"))
