n = 100
r = True
i = 1
for i in range(1,n):
    r = True
    if(i%3==0):
        r = False
        if(i%5==0):
            print("FizzBuzz, ")
        else:
            print("Fizz, ")
    elif(i%5==0):
        r = False
        print("Buzz, ")
    if(r==True):
        print(i,",")
