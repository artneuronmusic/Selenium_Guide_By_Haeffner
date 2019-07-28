from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
#import tempfile
import os
import time
import shutil

class DownLoad(unittest.TestCase):

    def setUp(self):

        options = Options() #whats the Options for?
        options.headless = True
        self.download_dir = "/Users/yuchienhuang/Desktop/auto_virtual/guide_book/python_tips/Download_tests"
        options.add_experimental_option("prefs", {
            "download.default_directory": self.download_dir,

            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })


        self.driver = webdriver.Chrome(chrome_options=options)




    def test_example_1(self):

        self.driver.get("http://the-internet.herokuapp.com/download")
        time.sleep(2)
        #self.driver.find_element_by_link_text("Ice_Cream_dessert_02.jpg").click()


        download_links = self.driver.find_elements_by_xpath("//div[@class='example']/a")

        for x in range(0, len(download_links)):
            if download_links[x].is_displayed():
                download_links[x].click()



        self.driver.find_element_by_link_text("some-file.txt").click()
        time.sleep(1.0)


        files = os.listdir(self.download_dir)
        files = [os.path.join(self.download_dir, i) for i in files] #add directory to each filename
        assert len(files) > 0 #check the directory is not empty
        #assert os.path.getsize(files[0]) > 0 #check the download file is not empty=>this has been error

        time.sleep(3)



    def tearDown(self):
        self.driver.quit()
        shutil.rmtree(self.download_dir)

if __name__ == "__main__":
    unittest.main()




#Initiate in "headless mode", where the browser saves time by not rendering the page: