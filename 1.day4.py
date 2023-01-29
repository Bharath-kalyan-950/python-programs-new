n=int(input("enter a number: "))
for i in range(n):
        if i % 5 == 0:
                print("buzz")
                continue
        elif i % 3 == 0:
                print("fizz")										
                continue
        elif (i % 5== 0) &(i %3==0):
                print("fizz,Buzz")
                continue
        print(i)
