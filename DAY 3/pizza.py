print("WELCOME TO PIZZA POINT")
size=input("WHAT SIZE PIZZA DO YOU WANT? S ,M ,L\n")
extra_cheese=input("DO YOU WANT exter cheese?  yes & no\n ")
add_pepperoeri=input(" DO YOU WANT exter pepperoeri?yes & no\n")
bill=0
if size=='S':
    bill+=5
elif size=='M':
    bill+=10
else:
    bill+=25
    
    
if add_pepperoeri=='Y':
    if size=='S':
     bill+=9
         else:
   bill+=25