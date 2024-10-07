import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Dictionary(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://www.merriam-webster.com/")
        time.sleep(2)

    def test_dictionary(self):

        search_line = self.driver.find_element(By.ID,"home-search-term")
        search_line.send_keys("QA"+Keys.ENTER)

        result = self.driver.find_element(By.CSS_SELECTOR,".dt>.dtText")

        self.assertEqual("quality assurance", result.text)


