students=input("Input the stusent of heigth ").split()
for n in range (0, len(students)):
    students[n]=int(students[n])
    print(students)
total_heigth=0
for heigth in students:
    total_heigth+=heigth
    print(total_heigth)
    number_