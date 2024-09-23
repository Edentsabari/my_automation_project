import unittest
from selenium import webdriver
from config import consts
from selenium.webdriver.common.by import By


class AppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(consts.BASE_URL)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

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
        self.assertEqual(consts.STUDENTS_TABLE,students_table.text)

    def test_students_table_content(self):
        students_table_rows = self.driver.find_elements(By.CSS_SELECTOR, '#studentsTable tbody tr')
        self.assertEqual(5, len(students_table_rows))



