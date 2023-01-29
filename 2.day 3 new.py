def dev(p):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (i!=j and j!=k and i!=k):
                    
                     print(p[i], p[j], p[k])
				
b=[]
n= int(input("enter no. of terms:"))
if(n>=4):
    print("invalid")
    n=int(input("enter a three digits only: "))
for v in range(0,n):
    m=int(input("enter a term :"))
    b.append(m)
  
dev(b)
