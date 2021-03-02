def sqrtnm(x):
    b = float(x) 
    for i in range(100): 
        x=0.5*(x + b/x) 
    return x
b=int(input("Enter number: "))
print("Square root of given number: ",sqrtnm(b))