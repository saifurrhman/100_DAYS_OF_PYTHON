student = input("Input a list of student heights ").split()
for n in range(0, len(student)):
  student[n] = int(student[n])
  print(student)
total_heigth=0
for heigth in student:
    total_heigth+=heigth
    print(total_heigth)
    number_of_student=0 
    for student in number_of_student:
        number_of_student+=1
        print(number_of_student )
    number_of_student= len(student)
    average_heigth=round (total_heigth/number_of_student )
    print(average_heigth)