import requests

response = requests.get("https://fakestoreapi.com/users/1")
results = response.json()

print(results, type(results))
print(results["username"])