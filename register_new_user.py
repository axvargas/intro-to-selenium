from unittest import TestCase, main
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver


class RegisterUser(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_btn = driver.find_element_by_xpath('//a[@title="Create an Account"]')
        self.assertTrue(create_account_btn.is_displayed() and create_account_btn.is_enabled())
        create_account_btn.click()

        self.assertEqual("Create New Customer Account", driver.title)

        firstname_input = driver.find_element_by_id('firstname')
        middlename_input = driver.find_element_by_id('middlename')
        lastname_input = driver.find_element_by_id('lastname')
        email_address_input = driver.find_element_by_id('email_address')
        password_input = driver.find_element_by_id('password')
        confirmation_input = driver.find_element_by_id('confirmation')
        register_btn = driver.find_element_by_xpath('//button[@title="Register"]')

        self.assertTrue(
            firstname_input.is_enabled()
            and middlename_input.is_enabled()
            and lastname_input.is_enabled()
            and email_address_input.is_enabled()
            and password_input.is_enabled()
            and confirmation_input.is_enabled()
            and register_btn.is_enabled()
        )

        firstname_input.send_keys('Test')
        driver.implicitly_wait(1)
        middlename_input.send_keys('Test')
        driver.implicitly_wait(1)
        lastname_input.send_keys('Test')
        driver.implicitly_wait(1)
        email_address_input.send_keys('test@test.com')
        driver.implicitly_wait(1)
        password_input.send_keys('Test')
        driver.implicitly_wait(1)
        confirmation_input.send_keys('Test')
        driver.implicitly_wait(1)
        register_btn.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="reports/resgister_user", report_name="register_user_test", add_timestamp=False))