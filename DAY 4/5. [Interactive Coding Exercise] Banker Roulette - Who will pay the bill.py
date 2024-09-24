import random
test_seed=int(input("CRETE A SEED NUMBER:"))
random.seed(test_seed)
nameasCSV=input("GIVE ME EVERYBOBY NAMES,SEPARETE BY A COMMMA  ")
NAME=nameasCSV.split(" , ")
# random.randint(0,9)
print(len(NAME))
num_items=len(nameasCSV)

random_choice=random.randint(0,num_items-1)
print(random_choice)