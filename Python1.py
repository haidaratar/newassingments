# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class DemoFacebook():
#     def demo_facebook(self):
#         options=webdriver.ChromeOptions()
#         options.add_experimental_option("detach",True)
#         Driver=webdriver.Chrome(options=options)
#         Driver.maximize_window()
#         Driver.implicitly_wait(30)
#         Driver.get("https://www.facebook.com/")
#         Driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
#         Driver.find_element(By.NAME,"firstname").send_keys("haidar")
#         Driver.find_element(By.NAME,"lastname").send_keys("Atar")
#
#
#
# dm=DemoFacebook()
# dm.demo_facebook()

l=['t','a','t',1,2,4,5,1,2]

emp_list=[]
dup_list=[]

for i in l:
    if i not in emp_list:
        emp_list.append(i)
        
    else:
        dup_list.append(i)



print(emp_list)
print(dup_list)
    
    
    
    
    