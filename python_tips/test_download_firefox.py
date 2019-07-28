import os
import time
import shutil
#import tempfile
import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

class Download(unittest.TestCase):
    """
    def setUp(self):
        self.download_dir = tempfile.mkdtemp() #make a temporary file and directory

        profile = webdriver.ChromeProfile()
        profile.set_preference("browser.download.dir", self.download_dir)
    """

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option()
        prefs = {
            "download.default_directory": r"/Users/yuchienhuang/Desktop/auto_virtual/guide_book/python_tips/test_download",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        self.driver = webdriver.Chrome(chrome_options=options)

    def tearDown(self):
        time.sleep()
        self.driver.quit()

    def test_example_1(self):
        driver = self.driver

        driver.get("http://the-internet.herokuapp.com/download")
        #download_link = driver.find_element_by_link_text("sampleUploadFile.png") #when the inspect has a
        download_link = driver.find_element_by_css_selector("//div[@class='example'/a]")
        download_link.click()

        time.sleep(1.0)

        files = os.listdir(self.prefs[0])






#we can be able to do is set the default download files location for the browser and allow it to automatically download the files.
#Python Selenium WebDriver will launch Firefox in default profile (Since no profile is specified explicitly). So in this case,
# we need to configure download location every time which is not expected in automation environment.