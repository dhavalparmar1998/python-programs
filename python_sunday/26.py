# import requests

# result = requests.get("https://jsonplaceholder.typicode.com/users")

# ans = result.json()
# print(type(ans))
# print(ans[0])

import json
userdata = '[{"name":"user1","age":20}]'

result = json.loads(userdata)
print(result , type(result))

userinfo = [{"name":"user2","age":21}]
print(userinfo , type(userinfo))

ans = json.dumps(userinfo)
print(ans , type(ans))