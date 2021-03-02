n=int(input("Enter range:"))
print("Prime numbers:",end=' ')
def prime():
    for x in range(1,n):
        for i in range(2,x):
            if(x%i==0):
                break
        else:
            print(x,end=' ')
    return 
prime()
        