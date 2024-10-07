import time
import unittest
from selenium import webdriver
from config import consts
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random

class NEXTPAGETest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get(consts.BASE_URL)
        time.sleep(2)

    def test_next_page(self):
        next_page_link = self.driver.find_element(By.LINK_TEXT,'Next Page')
        next_page_link.click()

        self.assertEqual(consts.NEXT_PAGE_URL,self.driver.current_url)

        self.assertEqual("Next Page",self.driver.title)

        change_title = self.driver.find_element(By.CSS_SELECTOR,"[onclick='changeTitle();']")
        change_title.click()

        self.assertEqual("Finish", self.driver.title)

        back_to_home = self.driver.find_element(By.LINK_TEXT,"Back to Home Page")
        back_to_home.click()

        self.assertEqual(consts.BASE_URL, self.driver.current_url)