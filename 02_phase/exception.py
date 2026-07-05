# num = int(input("Number:"))
# print(num)

# try:
    # a= int(input("number"))
    # b= int(input("number"))
    # result = a / b
    


# except (ValueError ,ZeroDivisionError):
    # print("Invalid operations")
# else :
    # print(result)



# raise exceptions

# age = int(input())
# if age < 18:
#    raise ValueError("Age must be at least 18.")


# amount = int(input("withdraw : "))

# if amount > balance:
#     raise Exception("Insf blnce")



class InsufficientBalanceError(Exception):
    pass

balance = 500


def deposit():
    global balance
    try:
        amount = int(input("amount :"))


        if amount <=0 :
            raise  ValueError("Invalid amount")
    except ValueError:
        print("invalid value")
    else :
        balance +=amount
        print("money deposited successfully" ,balance)
    finally:
        print("end")
    


deposit()