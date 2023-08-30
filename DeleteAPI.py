from selenium import webdriver
from selenium.webdriver.common.by import By


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
Driver=webdriver.Chrome(options=options)
Driver.maximize_window()
Driver.implicitly_wait(30)

Driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
Driver.find_element(By.ID,"autosuggest").send_keys("Ind")

allcountries=Driver.find_elements(By.XPATH,"//a[@class='ui-corner-all']")
print("The total number countries is:-",len(allcountries))


for country in allcountries:
    if country.text=="India":
        country.click()
        break
    
    
