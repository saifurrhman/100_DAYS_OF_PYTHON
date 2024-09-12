a=float(input("ENTER THE FIRST NUMBER: "))
b=float(input("ENTER THE SECOND NUMBER: "))
operation=input("enter the operation (+,-*,/)")
if operation =='+':
    result= a+b
elif operation =='-':
    result= a-b
elif operation =='*':
    result= a*b
elif operation =='/':

    if b!=0:
      result= a/b
    else :
        result= "error"
    
else:
     result = "Invalid operation!"
print(f"Result: {result}")
