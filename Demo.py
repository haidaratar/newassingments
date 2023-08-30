import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl.workbook.workbook import Workbook



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
Driver = webdriver.Chrome(options=options)
Driver.maximize_window()
Driver.implicitly_wait(30)

Driver.get("https://www.amazon.in/")
product="Samsung Mobile"
Driver.find_element(By.ID,"twotabsearchtextbox").send_keys(product)
Driver.find_element(By.ID,"nav-search-submit-button").click()

PhoneName=Driver.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
PhonePrice=Driver.find_elements(By.XPATH,"//span[@class='a-price-whole']")

myphone=[]
myprice=[]

for name in PhoneName:
    myphone.append(name.text)
    
    
    
for price in PhonePrice:
    myprice.append(price.text)
    
    
FinalList=zip(myphone,myprice)

wb=Workbook()

wb['Sheet'].title="Product Details"

sh=wb.active
sh.append(['Name','Price'])

for i in list(FinalList):
    sh.append(i)
    
wb.save("Samsung Mobile data.xlsx")
wb.close()

time.sleep(4)
Driver.close()


