add = lambda a, b : a+b

print(add(3,4))

# syntax
# lambda paramters : expressions 

sq = lambda x:x * x
print(sq(5))



students = [
    ("John", 90),
    ("Alice", 80),
    ("Bob", 95)
]


students.sort(key=lambda student: student[1])

print(students)