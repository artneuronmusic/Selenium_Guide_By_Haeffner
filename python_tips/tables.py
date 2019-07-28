
import unittest
from selenium import webdriver




class TestHovers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):

        self.driver.quit()

    def test_example_1(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/tables")
        #driver.find_element_by_css_selector('#table1 thead tr th:nth-of-type(4)').click()
        #due_column = driver.find_elements_by_css_selector('#table1 tbody tr td:nth-of-type(4)')
        #dues = [float(due.text.replace("$", "")) for due in due_column]
        #assert dues == sorted(dues, reverse=True) #Email column
        driver.find_element_by_css_selector('#table1 thead tr th:nth-of-type(3)').click()
        email_column = driver.find_elements_by_css_selector('#table1 tbody tr td:nth-of-type(3)')
        emails = [email.text for email in email_column]
        assert emails == sorted(emails)