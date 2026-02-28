
"""
#number is prime or nahh

n = 12

count = 0

for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("prime")
else:
    print("not prime")
"""
"""
# prime numbers between 1 to 100
for num in range(1,1001):
        count = 0
        for i in range(1,num+1):
            if num%i==0:
                count=count+1
        if count==2:
            print(i)
"""
"""
for i in range(1,6):
    for j in range(1,6):
        print("*",end='')
    print("")
"""
"""
for i in range(1,6):
    print("*"*i)
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print("")
"""

"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print("")
"""
"""
m = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(m,end='')
        m=m+1
    print("")
"""
"""
m = 1
for i in range(1,6):
    for j in range(1,i+1):
        print(m%2,end='')
        m=m+1
    print("")
"""
"""
for i in range(1,6):
    print(str(i)*i)
"""
"""
m = ""
for i in range(1,6):
        m=m+str(i)
        print(m)
"""
"""
m = 1
for i in range(1,6):
    m = 5-i
    print(" "*m,"*"*i)

for i in range(1,6):
    print(" "*(5-i),"*"*i)
"""
"""
for i in range(1,6):
    print(" "*(5-i)," *"*i)
"""
"""
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end='')
    print("")
"""
"""
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end='')
    print("")
"""
"""
m = 65
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(m),end='')
        m=m+1
    print("")
"""
"""
m = ""
for i in range(65,70):
        m=m+chr(i)
        print(m)
"""
"""
12344321
123**321
12****21
1******1

for i in range(4,0,-1):
    for j in range(1,5):
        if i>=j:
            print(j,end='')
        else:
            print("*",end='')
    for j in range(4,0,-1):
        if i>=j:
            print(j,end='')
        else:
            print("*",end='')
    print("")
"""

m = "0"
for i in range(10,0,-1):
    if i!=10:
        m = str(i)+m+str(i)
    print(m)













































































































