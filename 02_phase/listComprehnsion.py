
iterable  = [1,2,3,4]

result = [item for item in iterable]


# ex - normalway
numbers=[]
for i in range(5):
    numbers.append(i)

# print(numbers)

# list comprehensions

num = [i for i in range(6)]
# print(num)


# ex - squares of num

sq = []

for i in range(1,6):
    sq.append(i * i)

# print(sq)

# comprehsion
sq = [i*i for i in range(1,6)]

# print(sq)

# ex - strings

names = ["Ali",  "jhon", "Hassan"]

upper = [name.upper() for name in names]

# print(upper)


# length of the strings

names = ["react", 'python', "node"]

lengths   = [len(name) for  name in names ]

# print(lengths)


# ex add 10

number = [1,2,3,4,5]

result = [x + 10 for x in number]

# print(result)

# even numbers

even = []

for i in range(10):
    if i % 2 == 0:
        even.append(i)


# in list comprehseion


evens = [ i*i  for i in range(10) if i% 2 == 0] 
# print(evens)

# another 

names = ["Hassan", "Hsr", "Raza", "Alexander"]

result = [name for name in names if len(name) > 4]

# print(result)

# flatten a matrix

matrix = [
    [1,2],
    [3,4],
    [5,6]
]

flat = [num for row in matrix for num in row]

print(flat)

