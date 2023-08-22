import requests


resp=requests.put("https://restful-booker.herokuapp.com/booking/:id")
print(resp.status_code)

# print(resp.json())
# print(resp['Content-Type'][0]['Content-Type']['totalprice'])
# assert resp['Content-Type'][0]['Content-Type']['totalprice']!=0



