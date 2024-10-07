import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from HomePage.config import consts

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
        self.driver.get(consts.BASE_URL)
        time.sleep(2)

    def test_dictionary(self):

        #פונקציה שנכנסת למילון דרך לחיצה על הלינק ומזינה את הערך QA וצפויה לקבל את ההסבר
        dictionary_page_link = self.driver.find_element(By.LINK_TEXT, 'Merriam-Webster Dictionary')
        dictionary_page_link.click()
        time.sleep(3)

        self.assertEqual(consts.DICTIONARY_PAGE_URL,self.driver.current_url)


        search_line = self.driver.find_element(By.ID,"home-search-term")
        search_line.send_keys("QA")
        self.driver.save_screenshot("../ScreenShots/dictionary_QA.png")
        search_line.send_keys(Keys.ENTER)
        result = self.driver.find_element(By.CSS_SELECTOR,".dt>.dtText")
        self.driver.save_screenshot("../ScreenShots/dictionary_result.png")
        self.assertEqual("quality assurance", result.text)
