import unittest
from selenium import webdriver
from config import consts
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random

class AppTest(unittest.TestCase):
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

    def test_browser_title(self):
        self.assertEqual(consts.BROWSER_TITLE, self.driver.title)

    def test_page_title(self):
        h1_list = self.driver.find_elements(By.TAG_NAME, 'h1')
        self.assertEqual(1, len(h1_list))
        self.assertEqual(consts.PAGE_MAIN_TITLE, h1_list[0].text)

    def test_existence_of_two_tables(self):
        table_list = self.driver.find_elements(By.TAG_NAME, 'table')
        self.assertEqual(2, len(table_list))

    def test_cities_table_name(self):
        cities_table = self.driver.find_element(By.ID, 'citiesOfTheWorldTitle')
        self.assertEqual(consts.CITIES_TABLE, cities_table.text)

    def test_students_table_name(self):
        students_table = self.driver.find_element(By.ID, 'studentDetailsTitle')
        self.assertEqual(consts.STUDENTS_TABLE, students_table.text)

    def test_students_table_content(self):
        students_name = consts.STUDENTS_FIRST_NAME
        first_name_column_idx = None
        table = self.driver.find_element(By.CSS_SELECTOR, '#studentsTable')
        table_body_rows = table.find_elements(By.CSS_SELECTOR, 'tbody tr')
        table_header_row_options = table.find_elements(By.CSS_SELECTOR, "thead th")
        self.assertEqual(5, len(table_body_rows))

        for idx, column in enumerate(table_header_row_options):
            if column.text == consts.FIRST_NAME_COLUMN:
                first_name_column_idx = idx
                break

        for row in table_body_rows:
            name_cell = row.find_element(By.XPATH, f".//td[{first_name_column_idx + 1}]")
            self.assertIn(name_cell.text, students_name)
            students_name.remove(name_cell.text)

