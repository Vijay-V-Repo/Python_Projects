m=int(input("Enter total terms:"))  
a,b=0,1
print(a)
print(b)
for i in range(1,m):
    c=a+b
    print(c)
    a,b=b,c