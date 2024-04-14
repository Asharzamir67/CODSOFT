x=int(input("enter first number:"))
y=int(input("enter second number:"))
operation=input("choose which operation you want to perform:\n+ , - , /, * :")
print("the value of x is:",x)
print("the value of y is:",y)
if operation=="+":
    sum=x+y
    print("the sum of two numbers are:",sum)
elif operation=="-":
    sub=x-y
    print("the difference of two numbers are:",sub)
elif operation=="*":
    mul=x*y
    print("multiplication of two numbers give:",mul)
elif operation=="/":
    div=x/y
    print("dividing two numbers give:",div)
else:
    print("wrong selection of arthematic operation")