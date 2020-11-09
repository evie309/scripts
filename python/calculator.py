def sum(a,b):

    return int(a)+int(b)

x = input("Enter first number:")
y = input ("Enter second number:")

if(x.isdigit() and y.isdigit()):
    sum = sum(x,y)
    print("sum=",sum)
else:
    print("Inputs are not integers")




    
