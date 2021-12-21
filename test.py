from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class SiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Safari()
        self.driver.get("https://ru.shein.com/?ref=www&rep=dir&ret=ru")
        self.driver.implicitly_wait(10)

    def test_01(self):
        driver = self.driver
        input_field = driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/div/div[2]/form/input")
        input_field.send_keys("ФЫВАПРОЛДЖЭ")
        input_field.send_keys(Keys.ENTER)

        driver.switch_to.frame(1)
        alert = driver.find_elements_by_xpath('//*[@id="product-list-v2"]/div[1]/div[2]/div/div[1]/span')
        assert ' не совпал ни с какими продуктами.' in alert.text

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()