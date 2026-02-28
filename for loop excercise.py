"""
Ans:1
for i in range(1,11,1):
    print(i)

Ans:2
for i in range(1,21,1):
    if i%2==0:
        print(i)

Ans:3
a=0
for i in range(1,10,1):
    a = a+i
print(a)

Ans:4
a = int( input("Whats the number:"))

for i in range(1,11,1):
    b=a*i
    print(b)

Ans:5
a="hello"
b=0
for char in a:
    b = b+1
print("Total Characters:",b)

Ans:6
for i in range(1,11,1):
    if i==5:
        break
    print(i)

Ans:7
a =(1,123,123,123,123,14,124,25,234,324)
for i in a:
    if i==25:
        print("Found")
        break

Ans:8
a =(1,123,123,123,123,14,124,25,-234,324)
for i in a:
    if i<0:
        print(i)
        break

Ans:9
for i in range(1,11,1):
    if i==5:
        continue
    print(i)    

Ans:10
for i in range(1,21,1):
    if i%2==0:
        continue
    print(i)    

Ans:11
a ="PHYTHON"
for i in a:
    if i=="O":
        continue
    print(i,end='')

Ans:12
for i in range(1,6,1):
        pass
        print(i)    

Ans:13
for i in range(1,11,1):
    if i==6:
        pass
    print(i)

Ans:14
a =(1,123,123,123,123,14,124,25,100,324)
for i in a:
    if i==100:
        print("Found")
        
    else:
        print("Not Found")

Ans:15
a = int(input("whats the numebr:"))

for i in range(2,a):
    if a%i==0:
        print("Not Prime Numeber")
        break
else:
    print("Prime Number")
    
Ans:16
for i in range(1,6,1):
    print("*"*i)

Ans:17
for i in range(1,6,1):
    a =6-i
    print("*"*a)

Ans:18
a = ""
for i in range(1,6):
    a = a+str(i)
    print(a)

Ans:19
a = ""
for i in range(1,6):
    a = str(i)*i
    print(a)

Ans:20
a = 0
b = 4
for i in range(1,11,2):
    a=a+i
    print(" "*b,"*"*i)
    b=b-1

Ans:21
a = 10
b = 0
for i in range(11,0,-2):
    a=a-i
    print(" "*b,"*"*i)
    b=b+1

Ans:22
a = 1
for i in range(1,5):
    print("*"*a)
"""











































    
    
