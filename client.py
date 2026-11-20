import requests
URL = "http://127.0.0.1:8001"
user_credentials = {"username":"harini", "password": "123456789","user_type": "admin" }
#register
# response = requests.post(url =URL+"/register", json = user_credentials)
# print(response.status_code)
# print(response.json())

#login
response = requests.post(url = URL+"/login", json = user_credentials)
response_json = (response.json())
access_token = response_json["access_token"]
refresh_token = response_json["refresh_token"]

#get packages
header = {"token": access_token}
response = requests.get(url=URL+"/packages", headers=header)
print(response.json())

#get packages by id
package_id = 1
response = requests.get(url=URL+f"/packages/{package_id}",headers=header)
print(response.json())

#add packages
package_data = {"name": "Laptop","destination": "Bengaluru","weight": 15,"arrival_date": "2026-11-16"}
response = requests.post(url=URL + "/packages",headers=header,json=package_data)
print(response.json())


#get dispatch batches
response = requests.get(url=URL+"/dispatch-batches",headers=header)
print(response.json())


