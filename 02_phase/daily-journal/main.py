from utils import add_to_dic , read_entries
def main():
    while True:
        print("1. Add")
        print("2. View")
        print("3. Exit")

        menu =None
        
        try:
            menu = int(input("Enter your choice: "))
        except ValueError:
            print("enter valid number 1- 3 \n ")
            continue

        if menu == 1:
            print("n--Add your entries -- \n")
            add_to_dic()

        elif menu == 2:
            print("--Your entries--\n")
            entries = read_entries()

            if not entries:
                print("No data found") 
            else:
                for entry in entries:
                    print(f"[{entry['created_at']}] {entry['title']}: {entry['content']}")
                
        elif menu == 3:
            print("GoodBye..")
            break

        else:
            print("Inavlid operation")

if __name__ =="__main__":
    main()

