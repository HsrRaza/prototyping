import requests


def query():
    user_id = int(input("Enter user Id : "))

    headers = {
    "User-Agent": "Python Learning App",
    "Accept": "application/json"
}

    
    params = {
           "userId":user_id,
           }
    response = requests.get(
              "https://jsonplaceholder.typicode.com/posts",
                 params=params ,
                 headers=headers
                 
           )
    print(response.headers)
    # posts = response.json()
    # count = len(posts)
    # for post in posts:
    #         print("Title :", post["title"])
    #         print("body  :", post["body"])
    #         print("-"*40) 
   
    # print(f"User {user_id} has {count} posts  ")

    
# query()



headers = {
    "User-Agent": "Python Learning App",
    "Accept": "application/json"
}

params = {
    "userId": 1
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params,
    headers=headers
)

print(response.status_code)
print(response.headers["Content-Type"])