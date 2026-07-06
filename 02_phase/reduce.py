from functools import reduce

numbers = [1,2,3,4,5]

results = reduce(
    lambda a,b :a+b
, numbers , 100)


# print(results)


# factorial

n= 5

fact = reduce(lambda a, b : a*b, range(1,  n+ 1))

# print(fact)

# sum of square

num= [1,2,3]

sq = reduce(lambda a, b :a+b, map(lambda x:x*x , num))

# print(sq)


employess = [
    {"salary" : 40000},
    {"salary" :60000},
    {"salary" :50000},
]

total = reduce(
    lambda total, emp: total+emp["salary"] ,employess,0
)
print(total)
