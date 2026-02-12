import requests

# params = {
# "limit": 1, # Number of quotes (1–50)
# "maxLength": 100, # Optional: max characters
# "tags": "inspirational" # Optional: filter by tags
# }
# response = requests.get(url="https://api.quotable.io/quotes/random",params=params)
# print(response)
# response.raise_for_status()
# data = response.json()
# print(data)
print(requests.get("https://www.google.com").status_code)