import time
import requests

url = "https://api.github.com/users/torvalds"

for i in range(5):
    response = requests.get(url)
    print(response.json())
    print("-"*40)
    print(i)
    print("-"*40)
    time.sleep(2)
    
