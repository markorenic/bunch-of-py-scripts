import random
def shuffledeck(list):
    #how many times to repeat the process, more iterations more shuffled the deck is
    pointer = len(list) - 1
    while pointer >= 0:
        i = pointer
        j = random.randint(0,pointer)
        temp = list[i]
        list[i]=list[j]
        list[j]=temp
        pointer = pointer - 1

list_ = [1,2,3,4,5,6,7,8,9,10]

shuffledeck(list_)
print(list_)