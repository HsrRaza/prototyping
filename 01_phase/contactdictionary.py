users = []


def add_contact (users):
    name = input("Enter your name")
    email = input("Enter your email")

    if '@' not in email:
        print("Invalid email")
        return



    for user in users:
        if user['email'] == email:
            print("email already exists")
            return 
    
    users.append({
    "name":name,
    "email":email,
 })
    



def search(users):

    search_input = input("Enter your name").lower()


    
    for user in users:
        if user['name'].lower() == search_input:
            print(user) 
            return
    
    print("Contact not found")
        


def delete_contact(users):
    name = input("Enter name").lower()

    for user in users:
        if user['name'] == name:
           users.remove(user)
           print("users deleted : ", user)
           return
    print("user not found")
        

  

def display_fnc(users):
    print('\n Contact List \n')

    for user in users:
        print(f"Name :{user['name']}")
        print(f"Email : {user['email']}")
        print("-" * 30)


def main():
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        try:
            menu = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number (1-5).")
            continue

        if menu == 1:
            add_contact(users)

        elif menu == 2:
            search(users)

        elif menu == 3:
            display_fnc(users)

        elif menu == 4:
            delete_contact(users)

        elif menu == 5:
            print("Thank you for using Contact Management System.")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")

     
if __name__ == "__main__":
    main()