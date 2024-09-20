import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ExampleFunctionalTest(unittest.TestCase):
    def setUp(self):
        # Use Service class to define the path to ChromeDriver
        service = Service('/opt/homebrew/bin/chromedriver')  # Adjust path if necessary
        self.browser = webdriver.Chrome(service=service)

    def tearDown(self):
        self.browser.quit()

    def test_heading_text_is_correct(self):
        self.browser.get("http://localhost:8000")
        element: WebElement = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual("Mental Health Tracker", element.text)

    def test_page_title_is_correct(self):
        self.browser.get("http://localhost:8000")
        self.assertEqual("PBP Mental Health Tracker", self.browser.title)

if __name__ == "__main__":
    unittest.main()
