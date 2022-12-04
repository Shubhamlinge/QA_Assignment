import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

serv_obj = Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")


# Test case For WebPage

class Test(unittest.TestCase):
    def testName(self):
        driver: WebDriver = webdriver.Edge(service=serv_obj)
        driver.get("https://www.saucedemo.com")
        titleOfWebpage = driver.title
        # verify title is saucedemo
        self.assertEqual("Swag Labs", titleOfWebpage, "Webpage title not matching")
        driver.close()

    # Test Case For Login
    def testLogin(self):
        driver: WebDriver = webdriver.Edge(service=serv_obj)
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        driver.find_element(By.ID, 'login-button').click()
        titteOfLoginPage = driver.title
        self.assertEqual("Swag Labs", titteOfLoginPage, "WebLogin tittle is not matching")
        driver.close()

    # Test Case For Invalid Login
    def testInvalid_Login(self):
        driver: WebDriver = webdriver.Edge(service=serv_obj)
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, 'user-name').send_keys("standard_us")
        driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        driver.find_element(By.ID, 'login-button').click()
        invalidOfLoginPage = driver.find_element_by_xpath("//h3[@data-test='error']").text
        print(invalidOfLoginPage)
        self.assertEqual("Epic sadface: Username and password do not match any user in this service",
                         invalidOfLoginPage, "Invalid Webpage")
        driver.close()


if __name__ == "__main__":
    unittest.main()