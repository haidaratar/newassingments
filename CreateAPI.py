import requests


payload={
    "firstname" : "Jim",
    "lastname" : "Brown",
    
}
    
resp=requests.post("https://restful-booker.herokuapp.com/booking",data=payload)
print(resp.status_code)
#print((resp.json()))



# assert resp.status_code==200, "code does not match"
# print(resp['Content-Type'][0]['firstname'])
# assert resp['Content-Type'][0]['firstname']!=None ,"first name not match"

