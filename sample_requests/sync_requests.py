import requests
import json

response = requests.get("http://127.0.0.1:8000/user/0", headers={})
print(response)

sample_data_to_send = {
    "name" : "bob",
    "liked_posts" : [1,2,3,4],
    "short_description" : "some short description", 
    "long_bio" : "some long bio"
}
json_data = json.dumps(sample_data_to_send)
print("json data : ", json_data)
post_response = requests.post("http://127.0.0.1:8000/user/", headers={}, data=sample_data_to_send)
print("post request response : ", post_response.json())

requests.delete()