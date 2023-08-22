import requests


resp=requests.get("https://restful-booker.herokuapp.com/booking/:id")
print(resp.status_code)

#print(resp.json())
#print(resp['Content-Type'][0]['lastname'])
#assert resp['Content-Type'][0]['lastname']!=None ,"last name not match"