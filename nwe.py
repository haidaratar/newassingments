import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl.workbook.workbook import Workbook


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
Driver=webdriver.Chrome(options=options)
Driver.maximize_window()
Driver.implicitly_wait(30)

Driver.get("https://sample-self-storage-staging.netlify.app/pay-rent/rent-sub/login")

Driver.find_element(By.ID,"username").send_keys("dhegde")
Driver.find_element(By.ID,"userpassword").send_keys("1234")
Driver.find_element(By.XPATH,"//button[text()='Login']").click()

Driver.find_element(By.XPATH,"//span[text()='Other Amount']").click()
Driver.find_element(By.XPATH,"//input[@type='number']").send_keys("10000")
assert Driver.find_element(By.XPATH,"//input[@type='number']"), "payment is not done"
Driver.find_element(By.XPATH,"(//input[@name='mode'])[position()=2]").click()
time.sleep(2)
Driver.find_element(By.XPATH,"//button[text()=' Make a Payment ']").click()

wb=Workbook

wb["Sheet"].title="Product Details"

sh=wb.active

sh.append(["Name","Title"])










