import unittest
from selenium import webdriver
from config import consts
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
from time import sleep

class FormTest(unittest.TestCase):
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

    def find_form_elements(self):
        self.first_name = self.driver.find_element(By.ID, "first-name")
        self.last_name = self.driver.find_element(By.ID, "last-name")
        self.email = self.driver.find_element(By.ID, "email")
        self.mobile = self.driver.find_element(By.ID, "mobile")

        self.city = self.driver.find_element(By.ID, "city")
        self.area_code = self.driver.find_element(By.ID, "area-code")

        self.female_btn = self.driver.find_element(By.ID, "female")
        self.male_btn = self.driver.find_element(By.ID, "male")
        self.other_btn = self.driver.find_element(By.ID, "other")
        self.math_btn = self.driver.find_element(By.ID, "math")
        self.physics_btn = self.driver.find_element(By.ID, "physics")
        self.biology_btn = self.driver.find_element(By.ID, "biology")
        self.chemistry_btn = self.driver.find_element(By.ID, "chemistry")
        self.english_btn = self.driver.find_element(By.ID, "english")

    def fill_form(self):
        self.find_form_elements()
        city_dropdown = Select(self.city)
        city_dropdown_options = self.driver.find_elements(By.CSS_SELECTOR, "#city option")

        area_code = Select(self.area_code)
        area_code_dropdown_options = self.driver.find_elements(By.CSS_SELECTOR, "#area-code option")
        selected_idx_city = random.randint(1, (len(city_dropdown_options) - 1))
        selected_idx_area_code = random.randint(1, (len(area_code_dropdown_options) -1 ))
        self.first_name.send_keys(consts.FORM_DATA.get('first_name'))
        sleep(0.5)
        self.last_name.send_keys(consts.FORM_DATA.get('last_name'))
        sleep(0.5)
        self.email.send_keys(consts.FORM_DATA.get('email'))
        sleep(0.5)
        self.mobile.send_keys(consts.FORM_DATA.get('mobile'))
        sleep(0.5)
        self.female_btn.click()
        sleep(0.5)
        self.biology_btn.click()
        sleep(0.5)
        self.chemistry_btn.click()
        sleep(0.5)
        city_dropdown.select_by_index(selected_idx_city)
        sleep(0.5)
        self.assertTrue(city_dropdown_options[selected_idx_city].is_selected())
        area_code.select_by_index(selected_idx_area_code)
        sleep(0.5)
        self.assertTrue(area_code_dropdown_options[selected_idx_area_code].is_selected())

    def check_form(self):
        self.find_form_elements()
        first_name_value = self.first_name.get_attribute("value")
        last_name_value = self.last_name.get_attribute("value")
        email_value = self.email.get_attribute("value")
        city_value = self.city.get_attribute("value")
        area_code_value = self.area_code.get_attribute("value")
        mobile_value = self.mobile.get_attribute("value")

        self.assertEqual("",first_name_value)
        self.assertEqual("",last_name_value)
        self.assertEqual("",email_value)
        self.assertEqual("Tel Aviv",city_value)
        self.assertEqual("050",area_code_value)
        self.assertEqual("", mobile_value)

        self.assertFalse(self.male_btn.is_selected())
        self.assertFalse(self.female_btn.is_selected())
        self.assertFalse(self.other_btn.is_selected())
        self.assertFalse(self.math_btn.is_selected())
        self.assertFalse(self.physics_btn.is_selected())
        self.assertFalse(self.biology_btn.is_selected())
        self.assertFalse(self.chemistry_btn.is_selected())
        self.assertFalse(self.english_btn.is_selected())

    def test_form(self):
        submit_form = self.driver.find_element(By.ID, "submit-form")
        self.fill_form()
        submit_form.click()

        reset_form = self.driver.find_element(By.ID,"reset-form")
        reset_form.click()

        self.check_form()


