import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
Driver=webdriver.Chrome(options=options)
Driver.maximize_window()
Driver.implicitly_wait(60)
Driver.get("https://www.google.com/")
Driver.find_element(By.NAME,"q").send_keys("amazon")
Driver.find_element(By.NAME,"btnK").click()
time.sleep(5)
Driver.find_element(By.XPATH,"//span[text()='Shop online at Amazon India - Great deals on Amazon']").click()

allpro=Driver.find_element(By.ID,"searchDropdownBox")
select=Select(allpro)
select.select_by_visible_text("Electronics")
Driver.find_element(By.ID,"twotabsearchtextbox").send_keys("dell computers")
Driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(2)
Driver.find_element(By.ID,"low-price").send_keys("30000")
Driver.find_element(By.ID,"high-price").send_keys("50000")
Driver.find_element(By.XPATH,"//input[@class='a-button-input']").click()

allcomputer=Driver.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
time.sleep(2)
allrate=Driver.find_elements(By.XPATH,"//span[text()='4.6 out of 5 stars']")

mycop=[]
myrate=[]


for comp in allcomputer:
    mycop.append(comp.text)
    mycop
    
for rate in allrate:
    myrate.append(rate.text)
    
   
FinalList=zip(mycop,myrate)

for data in list(FinalList):
    print(data)
    

    
    


    
    

    

    




