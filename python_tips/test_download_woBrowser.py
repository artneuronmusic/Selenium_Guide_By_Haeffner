import unittest
from selenium import webdriver
import http.client
import time

class RevisedDownload(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_example1(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/download")
        download_link = driver.find_element_by_xpath("//div[@class='example']/a").get_attribute('href')
        # for x in range(0, len(download_links)):
        #     if download_links[x].is_displayed():
        #         download_links[x].get_attribute('href')
        time.sleep(3)

        connection = http.client.HTTPConnection("the-internet.herokuapp.com")
        connection.request('HEAD', download_link)
        response = connection.getresponse()
        content_type = response.getheader('Content-type')
        content_length = response.getheader('Content-length')


        assert content_type == "application/octet-stream"   #The MIME type, which in this example is “Application”, is separated by a forward slash (“/”) and followed by a subtype.]
        #assert content_length > 0

if __name__ == "__main__":
    unittest.main()


    #arbitrary binary data"

    """
    Content-Type: application/octet-stream
    Content-Disposition: attachment; filename="picture.png"
    Means "I don't know what the hell this is. Please save it as a file, preferably named picture.png".

    Content-Type: image/png
    Content-Disposition: attachment; filename="picture.png"
    Means "This is a PNG image. Please save it as a file, preferably named picture.png".

    Content-Type: image/png
    Content-Disposition: inline; filename="picture.png"
    Means "This is a PNG image. Please display it unless you don't know how to display PNG images. Otherwise, or if the user chooses to save it, we recommend the name picture.png for the file you save it as".
    """