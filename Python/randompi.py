import random
import string

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def hash(array):
    i , product = 0 , 1
    while i < len(array):
        product, i = product * ord(array[i]), i + 1
    var = product % 10**1
    print(var)

array = list(input("Write a sentince boy: "))
hash(array)


product = 0
i = 0
var = 1
while var != product:
    array = list(randomString())
    product = hash(array)
    i = i + 1


