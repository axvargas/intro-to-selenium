from unittest import TestCase, main
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class Tables(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_name_elements(self):
        driver = self.driver
        number_of_columns = len(driver.find_elements_by_xpath('//table[@id="table1"]/thead/tr/th'))
        number_of_rows = len(driver.find_elements_by_xpath('//table[@id="table1"]//tr'))

        print(number_of_rows)
        print(number_of_columns)
        table_data = []
        print(table_data)
        for i in range(number_of_rows):
            row=[]
            for j in range(number_of_columns):
                if i==0:
                    # Header
                    data =driver.find_element_by_xpath(f'//table[@id="table1"]/thead/tr/th[{j+1}]')
                else:
                    # Body
                    data = driver.find_element_by_xpath(f'//table[@id="table1"]/tbody/tr[{i}]/td[{j+1}]')
                row.append(data.text)
            table_data.append(row)
        print(table_data)


    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="tables", report_name="test_tables"))
