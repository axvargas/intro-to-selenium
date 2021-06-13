from unittest import TestCase, main
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class AddRemoveElements(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input('How many elements do you want to add?: '))
        elements_removed = int(input('How many elements do you want to remove?: '))
        total_elements = elements_added - elements_removed
        add_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="example"]/button')))
        for i in range(elements_added):
            add_btn.click()

        for i in range(elements_removed):
            try:
                delete_btn = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="elements"]/button')))
                delete_btn.click()
            except:
                print('You are trying to delete more elements than the available')
                break
        
        sleep(5)
        if total_elements > 0:
            print(f'There are {total_elements} in the screen')
        else:
            print(f'There are 0 in the screen')

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="add_remove", report_name="test_add_remove"))