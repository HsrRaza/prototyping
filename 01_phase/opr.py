age  = 20
salary = 50000

if(age > 18 and salary > 40000):
    print("Eligible for loan")


# for i in range(0 , 10 ,2):
#     print(i)

# for i in range(2 , 5):
#     print(i)


# for i in range(10, 0 , -1):
    # print(i)


# while loop
# i = 1
# while(i <= 5):
    # print(i)
    # i +=1

# break means stop loop

# for i in range(10):
#     if(i==5):
#         break
#     print(i)


# continue means skip the current iteration and continue with the next iteration

# for i in range(5):
#     if(i==2):
#         continue
#     print(i)

numbers  = [1,2,3,4,5]

numbers[1] = 100
numbers.append(6)
numbers.remove(3)
# print(numbers)
# print(len(numbers))


# for i in numbers:
#     print(i)

person = ("Hassan" , 22)
# print(person)

user = {
    "name":"hassan",
    "age": 22,

}
# print(user["name"])

# update the value of a key in a dictionary
user['name'] = "Hsr"
# print(user["name"])

user["city"] = "Blr"

# loop for dictionary
# for key, value  in user.items():
    # print(key, value)

# nums = {1,2,3,4,5}

# if 3 in nums:
#     print("3 is present in the set")


# function

# function to add two numbers

def add(a,b):
    return a+b

res = add(5, 10)
# print(res)

# default parameters 

def greet(name = "Guest"):
    print("Hello "+ name)

# greet() #default  parameters will be used 
# greet("Hsr")

# keyword arguments

def user(name , age):
    print(name, age)

user(age=22, name="Hsr") # keyword arguments Order doesn't matter when using keyword arguments.

# Returning Multiple Values

# Python can return multiple values as a tuple.

def calculate(a ,b):
    return a+b, a-b, a*b, a/b

sum_val,  diff_val, prod_val, div_val = calculate(10, 5)
# print(sum_val, diff_val, prod_val, div_val)
print("Sum:", sum_val)
print("Difference:", diff_val)
print("Product:", prod_val)
print("Division:", div_val)

