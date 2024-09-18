print("WELCOME TO THE RIDE")
height = int(input("Your height in cm: "))

if height >= 140:
    print("You can easily apply.")
    age = int(input("Your age: "))
    if age >= 18:
        print("You can ride it!")
    else:
        print("You cannot ride, you are too young.")
else:
    print("Sorry, you are not tall enough to ride.")
