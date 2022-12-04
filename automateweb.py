import time

import self as self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\chromedriver.exe")
driver: WebDriver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.get("https://meralda.scalenext.io/user/register")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys('Shubhamm')
driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[1]/div/div[1]/div[2]/input").send_keys("Lingee")
driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[1]/div/div[2]/input").send_keys("shubhamlinge379@gmail.com")
driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[1]/div/div[3]/input").send_keys("8669158884")
driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[1]/div/div[4]/div/div/div/input").send_keys('2022-11-11')
driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[1]/div/div[5]/input").send_keys("Shubh@20233")
driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[1]/div/div[6]/input").send_keys("Shubh@20233")
time.sleep(5)
#driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/form/div/div[2]/button").click()
titteOfLoginPage = driver.title
self.assertEqual("MERALDA || HOME", titteOfLoginPage, "WebLogin tittle is not matching")
time.sleep(5)

driver.get("https://meralda.scalenext.io/user/login")
driver.find_element(By.XPATH,"//input[@placeholder='Email/Phone']").send_keys("shubhamlinge379@gmail.com")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("Shubh@20233")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

titteOfLoginPage = driver.title
self.assertEqual("MERALDA || HOME", titteOfLoginPage, "WebLogin tittle is not matching")