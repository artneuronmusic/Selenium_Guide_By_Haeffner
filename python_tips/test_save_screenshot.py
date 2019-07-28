from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import time

from IPython.display import Image
from PIL import Image
import image




class SaveScreenShot(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        prefs = {"download.default_directory": "/Users/yuchienhuang/Desktop/auto_virtual/guide_book/python_tips/screen/",
                 "directory_upgrade": True,

                 }
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(chrome_options=options)

    def tearDown(self):
        self.driver.quit()

    def test_screen(self):


        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.find_element_by_partial_link_text("File Download").click()
        self.driver.save_screenshot("screen_file3.png")
        time.sleep(3)
        size = (0, 0, 680, 400)
        im1 = Image.open("screen_file3.png")
        im2 = im1.crop(size)
        im2.save('element_image.png')




if __name__ == "__main__":
    unittest.main()


#driver.get_screenshot_as_file()

#plz refer to reference and next step is to put the new file into old folder