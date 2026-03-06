"""
#Part 1 - Basic Level
Ans:1
a = 1
while a<=10:
    print(a)
    a+=1

Ans:2
a = 1
while a<=20:
    if a%2==0:
        print(a)
    a+=1

Ans:3
a = 1
while a<=20:
    if a%2==1:
        print(a)
    a+=1

Ans:4
a = 10
while a>=1:
    print(a)
    a-=1

Ans:5
a=1
while a<=100:
    if a%5==0:
        print(a)
    a=a+1

#Part 2 – Intermediate Level

Ans:6
a=1
b=0
while a<=10:
    a=1+a
    b=b+a
print(b)

Ans:7
a = int(input("Whats the Number:"))
b=1
while b<=a:
    if a%b==0:
        print(b)
    b+=1

Ans:8
a = int(input("Whats the Number:"))
b = 0
while a>0:
    a = a//10
    b=b+1  
print(b)

Ans:9
a = int(input("Whats the Number:"))
b=0
c = a
while c>0:
    d = c%10
    b=b*10 + d
    c = c//10
print(b)

Ans:10
a = int(input("Whats the Number:"))
b=0
c = a
while c>0:
    d = c%10
    b=b*10 + d
    c = c//10
if b==a:
    print("Yes")
else:
    print("Not")

Part 3 – Pattern Based

Ans:11
a=1
while a<=5:
    print("*"*a)
    a=a+1

Ans:12
a=1
b=""
while a<=5:
    b=b+str(a)
    print(b)
    a+=1

#Part 4 – Logical / Real Scenario

Ans:13
a=input("Enter Password:")

while a!="HappyHappy123":
    print("Retry")
    a=input("Enter Password:")
print("Logged in")

Ans:14

import random

a = random.randint(1,10)

while True:
    b = int(input("Choose a number between 1 and 10"))
    if a==b:
        print("You win")
        break
    print("Wrong guess")








Ans:15
a=int(input("Enter Number:"))
b=0
while a!=0:
    b=b+a
    a=int(input("Enter Number:"))
print(b)


#Bonus Challenge (Interview Level)

Ans:16

num = int(input("how many numbers you want?:"))
a = 0
b = 1
for i in range(num):
    c = a+b
    print(c)
    a = b
    b = c


Ans:17
a = int(input("Whats the Number:"))
b=a
c = 0
e=len(str(a))
f=0
while b>0:
    d = b%10
    f+=d**e
    b//=10
if f==a:
    print("Yes")
else:
    print("Not")

Ans:18

a = 2
while a<=50:
    b=2
    c=0
    while b<a:
        if a%b==0:
            c=1
            break
        b+=1
    if c==0:
        print(a)
    a+=1

"""




































































