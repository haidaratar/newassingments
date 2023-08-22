import requests


resp=requests.delete("https://restful-booker.herokuapp.com/booking/1")
print(resp.status_code)

#print(resp.json())
# print(resp['Cookie'][1])
# assert resp['Cookie'][1]==204, "Booking not deleted "

