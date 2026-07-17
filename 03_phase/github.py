import requests



def get_user(user):
    response = requests.get(f"https://api.github.com/users/{user}")

    if response.status_code == 200:

        users = response.json()
        # print(users)

        # print("\n")

        print("username  :" , users["login"])
        print("Name      :", users["name"])
        print("Company   :" ,users["company"])
        print("Location  :", users["location"])
        # print("Bio       :" ,users["bio"])
        print("created   :", users["created_at"])
    else:
        print("User not found")

    
    

get_user("torvalds")


