i=int(input())     
n=int(input())
m=i
for x in range(0,n-1):
    m=m+200
    i=i+m
    x=x+1
print(i)