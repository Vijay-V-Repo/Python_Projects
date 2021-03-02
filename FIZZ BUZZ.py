for i in range(1,101):
    if (i%3==0 and i%5==0):
        print(i,"FIZZ BUZZ")
    else:
        if i%3==0:
            print(i," - FIZZ")
        else:
            if i%5==0:
                print(i," - BUZZ")
            else:
                print(i)
                
                