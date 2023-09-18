# import requests
#
#
# resp=requests.get("https://reqres.in/api/users?page=2")
# print(resp.status_code)
# assert resp.status_code ==200 , "code does not match"
#
# json_resp=resp.json()
# #print(json_resp)
#
# print(json_resp["data"][0-4])


from selenium import webdriver
from selenium.webdriver.common.by import By



options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
Driver=webdriver.Chrome(options=options)
Driver.maximize_window()
Driver.implicitly_wait(60)
Driver.get("https://money.rediff.com/gainers?_gl=1*1q7xwwk*_ga*MTYwNzY1MzA5Ni4xNjgzNzMyNzIw*_ga_3FM4PW27JR*MTY5NDg3ODQ4NS45LjAuMTY5NDg3ODQ4NS4wLjAuMA..")

color=Driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[1]/td[5]").value_of_css_property('color')
print(color)



    


















