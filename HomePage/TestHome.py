import unittest
from selenium import webdriver
from config import consts
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import random
from time import sleep

class TestHome(unittest.TestCase):
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

#בדיקת title
    def test_browser_title(self):
        self.assertEqual(consts.BROWSER_TITLE, self.driver.title)

#בדיקה של כותרת הדף מכילה את הטקסט הנדרש ושקיים רק אלמנט אחד מסוג h1
    def test_page_title(self):
        h1_list = self.driver.find_elements(By.TAG_NAME, 'h1')
        self.assertEqual(1, len(h1_list))
        self.assertEqual(consts.PAGE_MAIN_TITLE, h1_list[0].text)

#לבדוק שקיים 2 טבלאות בדיוק
    def test_existence_of_two_tables(self):
        table_list = self.driver.find_elements(By.TAG_NAME, 'table')
        self.assertEqual(2, len(table_list))

#לבדוק שהכותרת של הטבלה הראשונה מכילה את הטקסט הנדרש
    def test_cities_table_name(self):
        cities_table = self.driver.find_element(By.ID, 'citiesOfTheWorldTitle')
        self.assertEqual(consts.CITIES_TABLE, cities_table.text)
#לבדוק שהכותרת של הטבלה השנייה מכילה את הטקסט הנדרש
    def test_students_table_name(self):
        students_table = self.driver.find_element(By.ID, 'studentDetailsTitle')
        self.assertEqual(consts.STUDENTS_TABLE, students_table.text)

#לבדוק שיש בדיוק 5 תלמידים ושהשמות פרטיים שלהם נכונים
    def test_students_table_content(self):
        students_name = consts.STUDENTS_FIRST_NAME
        first_name_column_idx = None
        table = self.driver.find_element(By.CSS_SELECTOR, '#studentsTable')
        table_body_rows = table.find_elements(By.CSS_SELECTOR, 'tbody tr')
        self.assertEqual(5, len(table_body_rows))
        names = []
        for row in table_body_rows:
            name = row.find_elements(By.TAG_NAME,'td')[1].text
            names.append(name)
        self.assertEqual(consts.STUDENTS_FIRST_NAME,names)

#עבודה עם טופס
    def find_form_elements(self):
        #פונקציה למציאת אלמנט מהטופס
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
        #פונקציה למילוי פרטים באלמנט
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
        sleep(3)
        self.assertTrue(area_code_dropdown_options[selected_idx_area_code].is_selected())

    def check_form(self):
        #בודק שהטופס ריק
        self.find_form_elements()
        first_name_value = self.first_name.get_attribute("value")
        last_name_value = self.last_name.get_attribute("value")
        email_value = self.email.get_attribute("value")
        city_value = self.city.get_attribute("value")
        area_code_value = self.area_code.get_attribute("value")
        mobile_value = self.mobile.get_attribute("value")
        sleep(2)
        self.assertEqual("",first_name_value)
        self.assertEqual("",last_name_value)
        self.assertEqual("",email_value)
        self.assertEqual("Tel Aviv",city_value)
        self.assertEqual("050",area_code_value)
        self.assertEqual("", mobile_value)
        sleep(2)
        self.assertFalse(self.male_btn.is_selected())
        self.assertFalse(self.female_btn.is_selected())
        self.assertFalse(self.other_btn.is_selected())
        self.assertFalse(self.math_btn.is_selected())
        self.assertFalse(self.physics_btn.is_selected())
        self.assertFalse(self.biology_btn.is_selected())
        self.assertFalse(self.chemistry_btn.is_selected())
        self.assertFalse(self.english_btn.is_selected())
        sleep(5)


    def test_form(self):
        #פונקציה ששולחת את הטופס ועושה מנקה את הטופס
        submit_form = self.driver.find_element(By.ID, "submit-form")
        sleep(2)
        self.fill_form()

        self.driver.save_screenshot("../ScreenShots/1_after_fill_form.png")
        submit_form.click()

        reset_form = self.driver.find_element(By.ID,"reset-form")
        sleep(2)
        reset_form.click()
        self.driver.save_screenshot("../ScreenShots/1_after_reset_form.png")
        self.check_form()
        sleep(2)


    def test_download(self):
        download = self.driver.find_element(By.CSS_SELECTOR,"[onclick='startDownload()']")

        self.driver.execute_script('arguments[0].scrollIntoView()', download)

        self.driver.save_screenshot("../ScreenShots/2_before_download.png")
        download.click()
        sleep(2)
        self.driver.save_screenshot("../ScreenShots/2_after_download_click.png")
        progress = self.driver.find_element(By.ID,"progress-txt")
        # Wait for 100%
        while progress.text!='100':
            pass

        self.driver.save_screenshot("../ScreenShots/2_after_download_finished.png")
        try:
            download_finished = self.driver.find_element(By.ID,"download-finished-msg")

            self.assertEqual("Download Finished! OK", download_finished.text)
        except NoSuchElementException:
            print("The 'Download Finished' element is not found")
            self.assertTrue(False)

        ok = self.driver.find_element(By.CSS_SELECTOR,"#download-finished-msg>button")
        sleep(5)
        ok.click()

        self.driver.save_screenshot("../ScreenShots/2_download_after_ok_click.png")
        # Check that the message disappeared
        self.assertEqual("",download_finished.text)

    def test_next_page(self):
        next_page_link = self.driver.find_element(By.LINK_TEXT,'Next Page')
        next_page_link.click()
        sleep(2)
        self.driver.save_screenshot("../ScreenShots/3_after_next_page.png")

        self.assertEqual(consts.NEXT_PAGE_URL,self.driver.current_url)

        self.assertEqual("Next Page",self.driver.title)

        change_title = self.driver.find_element(By.CSS_SELECTOR,"[onclick='changeTitle();']")
        change_title.click()
        sleep(5)
        self.driver.save_screenshot("../ScreenShots/3_after_change_title.png")

        self.assertEqual("Finish", self.driver.title)

        back_to_home = self.driver.find_element(By.LINK_TEXT,"Back to Home Page")
        back_to_home.click()
        sleep(5)
        self.driver.save_screenshot("../ScreenShots/3_after_back_to_home.png")

        self.assertEqual(consts.BASE_URL, self.driver.current_url)


