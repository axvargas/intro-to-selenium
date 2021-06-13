from unittest import TestCase, main
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class AddRemoveElements(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver
        options = []
        no_options = 5
        tries = 1

        while len(options) < 5:
            options.clear()
            for i in range(no_options):
                try:
                    option_name = driver.find_element_by_xpath(f'//ul/li[{i+1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f'Option number {i+1} was NOT FOUND')
                    tries += 1
                    driver.refresh()
        
        print(f'Finished in {tries} tries')

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
            output="dinamic_elements", report_name="test_dinamic_elements"))