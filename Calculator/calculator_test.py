import time
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Calculator(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://www.calculator.net/")
        time.sleep(5)

    def test_calc_result(self):

        #פונקציה שלוחצת על 7 ועל 5 ומתקבל הסכום
        num7 = self.driver.find_element(By.CSS_SELECTOR,"[onclick='r(7)']")
        num5 = self.driver.find_element(By.CSS_SELECTOR,"[onclick='r(5)']")
        mult_operator = self.driver.find_element(By.XPATH,"//*[text()='+']")
        eq_operator = self.driver.find_element(By.XPATH,"//*[text()='=']")
        result = self.driver.find_element(By.ID, "sciOutPut")

        num7.click()
        sleep(0.5)
        mult_operator.click()
        sleep(0.5)
        num5.click()
        sleep(0.5)

        eq_operator.click()
        sleep(0.5)

        #ScreenShot
        self.driver.save_screenshot('../ScreenSHots/calculator_result.png')

        self.assertEqual(" 12",result.text)



