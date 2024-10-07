import unittest
from selenium import webdriver
from config import consts
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import random
from time import sleep

class DownloadTest(unittest.TestCase):
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

    def test_download(self):
        download = self.driver.find_element(By.CSS_SELECTOR,"[onclick='startDownload()']")
        download.click()

        progress = self.driver.find_element(By.ID,"progress-txt")
        # Wait for 100%
        while progress.text!='100':
            pass

        try:
            download_finished = self.driver.find_element(By.ID,"download-finished-msg")

            self.assertEqual("Download Finished! OK", download_finished.text)
        except NoSuchElementException:
            print("The 'Download Finished' element is not found")
            self.assertTrue(False)

        ok = self.driver.find_element(By.CSS_SELECTOR,"#download-finished-msg>button")
        ok.click()

        # Check that the message disappeared
        self.assertEqual("",download_finished.text)

