import requests
# to run :python3 request_get_example.py
url = "http://192.168.1.22:8080/data?val=test"

def sendget(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Request successful!")
        print("Content:")
        print(response)  # Assuming the response is JSON
    else:
        print(f"Request failed with status code: {response.status_code}")
    return response

test = sendget(url)

