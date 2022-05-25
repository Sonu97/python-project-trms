import time

from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome("C:/Users/SonuP/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("http://localhost:63342/home_controller.py/view/addemp.html")

empid = WebElement = driver.find_element(by=By.ID, value="empidInput").send_keys("79")
password = WebElement = driver.find_element(by=By.ID, value="passwordInput").send_keys("pass897")
name = WebElement = driver.find_element(by=By.ID, value="nameInput").send_keys("Emily Miller")
email = WebElement = driver.find_element(by=By.ID, value="emailInput").send_keys("miller@gmail.com")
supervisorempid = WebElement = driver.find_element(by=By.ID, value="supervisorempidInput").send_keys("30")
isdepthead = WebElement = driver.find_element(by=By.ID, value="isdeptheadInput").send_keys("no")
isbenco = WebElement = driver.find_element(by=By.ID, value="isbencoInput").send_keys("no")
isadmin = WebElement = driver.find_element(by=By.ID, value="isadminInput").send_keys("no")
deptid = WebElement = driver.find_element(by=By.ID, value="deptidInput").send_keys("4")
regemp = WebElement = driver.find_element(by=By.NAME, value ='regEmp()').click();
time.sleep(0.7)

driver.close()
