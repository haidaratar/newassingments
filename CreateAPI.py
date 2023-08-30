import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# Driver = webdriver.Chrome(options=options)
# Driver.maximize_window()
# Driver.implicitly_wait(30)

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
Driver=webdriver.Chrome(options=options)
Driver.maximize_window()
Driver.implicitly_wait(30)

Driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
Driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(3)

Products=Driver.find_element(By.XPATH,"//div[@class='products']")
time.sleep(4)
allitem=Products.find_elements(By.XPATH,"//button[text()='ADD TO CART']")
time.sleep(3)


for product in allitem:
    time.sleep(2)
    product.click()
    
Driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
time.sleep(2)
Driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

wait=WebDriverWait(Driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@class='promoCode']")))
Driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
Driver.find_element(By.XPATH,"//button[text()='Apply']").click()
Driver.find_element(By.XPATH,"//button[text()='Place Order']").click()

allcountry=Driver.find_element(By.XPATH,"//select")
country=Select(allcountry)
country.select_by_visible_text("India")
time.sleep(2)
Driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
Driver.find_element(By.XPATH,"//button[text()='Proceed']").click()


    






    
    
    










