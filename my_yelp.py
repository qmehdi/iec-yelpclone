import requests

api_key = "Hz720QO1M7QmyOsFgT5aB8k9_Otoejxnk2k7KE8j6XN-HpS-b-qmSPAs0_E53xtRpNsqkSi3K3X46JrgRUGoVLG9fs8BUBD4qGk9yWNpKqMLrnGkwNpR5BYgR-4MX3Yx"

url = "https://api.yelp.com/v3/businesses/search"

my_headers = {
    "Authorization": "Bearer {}".format(api_key)
}

my_params = {
    "term": "restaurants",
    "location": "chicago",
    "limit": 3,
}

businesses_object = requests.get(url, headers=my_headers, params=my_params)

businesses_dict = businesses_object.text

print(businesses_dict)