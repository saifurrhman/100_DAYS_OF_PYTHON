heigth=float(input("ENTER THE HEIGTH:"))
weigth=float(input("ENTER THE weigth:"))
bmi=round(weigth/heigth**2,2)
if bmi <18.5:
    print(f"your bmi is {bmi} you are uderr weigth")
elif bmi<25:
     print(f"your bmi is {bmi} you are  moramlweigth")
elif bmi<30:
     print(f"your bmi is {bmi} you are  overweigth")
elif bmi<35:
     print(f"your bmi is {bmi} you are obse ")
else :
    print(f"your bmi is {bmi} you are cically  ")
