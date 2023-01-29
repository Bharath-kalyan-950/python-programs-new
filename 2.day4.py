n=int(input("enter total users :"))
while(n<=0):
    if(n<=0):
        print("invalid")
        n=int(input("enter again total number of users :"))
m=int(input("enter staff users :"))
s=n-m
a=m/3
print("non teaching staff users=",a)
print("student users: ",s-a)
