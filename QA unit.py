import unittest
import self as self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\chromedriver.exe")

class Test(unittest.TestCase):
    def test_Name(self):
        driver:WebDriver=webdriver.Chrome(service=serv_obj)
        driver.get("https://meralda.scalenext.io/user/register")
        titleOfWebpage = driver.title
        #verify title is meralda
        self.assertEqual("Meralda || Register", titleOfWebpage, "Webpage title not matching")  # add assertion here
        driver.close()

    def test_validation(self):
        driver:WebDriver=webdriver.Chrome(service=serv_obj)
        driver.get("https://meralda.scalenext.io/user/register")
        #Verify Validation of registation Page
        driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[2]/button").click()
        alrt=driver.switch_to.alert.text()
        self.assertEqual("Please fill out this field.",alrt,"Not matching validation")
        driver.close()

    def test_fillform(self):
        driver: WebDriver = webdriver.Chrome(service=serv_obj)
        driver.get("https://meralda.scalenext.io/user/register")
        #verify All dropdown and checkbox
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys('Shubham')
        driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[1]/div/div[1]/div[2]/input").send_keys("Linge")
        driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[1]/div/div[2]/input").send_keys("shubhamlinge39@gmail.com")
        driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[1]/div/div[3]/input").send_keys("8669158804")
        driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[1]/div/div[4]/div/div/div/input").send_keys('2022-11-10')
        driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[1]/div/div[5]/input").send_keys("Shubh@2023")
        driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[1]/div/div[6]/input").send_keys("Shubh@2023")
        driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div[2]/form/div/div[2]/button").click()
        titteOfLoginPage = driver.title
        self.assertEqual("MERALDA || HOME", titteOfLoginPage, "WebLogin tittle is not matching")
        driver.close()

    def test_loginagain(self):
        driver: WebDriver = webdriver.Chrome(service=serv_obj)
        driver.get("https://meralda.scalenext.io/user/login")
        #verify registered user login again
        driver.find_element(By.XPATH, "//input[@placeholder='Email/Phone']").send_keys("shubhamlinge39@gmail.com")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Shubh@2023")
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        titteOfLoginPage = driver.title
        self.assertEqual("MERALDA || HOME", titteOfLoginPage, "WebLogin tittle is not matching")
        driver.close()

if __name__ == '__main__':
    unittest.main()
