"""
Ans:1
a = int( input("what's the number:"))
if a<0:
    print("Negative")
else:
    print("Positive")

Ans:2
a = int( input("what's the age:"))
if  a>=18:
    print("Eligible to vote")
else:
    print("Ineligible to vote")

Ans:3
a = int( input("what's the number:"))
if a%7==0:
    print("its divisable")
else:
    print("its not divisable")

Ans:4
a = int( input("what's the marks:"))
if a>=40:
    print("pass")
else:
    print("fail")

Ans:5
a = int( input("what's the number:"))
if a>=100:
    print("Greater than 100")
else:
    print("Smaller than 100")

Ans:6
a = int( input("what's the temperature:"))
if a>=45:
    print("hotter than 45°c")
else:
    print("colder than 45°c")

Ans:7
a = int( input("what's the lenght of the string:"))
if a>=8:
    print("longer than 8 characters")
else:
    print("smaller than 8 characters")

Ans:8
a = input("Type password:")
if a=="admin123":
    print("Logged In ")
else:
    print("wrong passward")

Ans:9
a = int( input("what's the number:"))
if a%10==0:
    print("Multiple of 10")
else:
    print("nope")

Ans:10
a = int( input("what's the Balance:"))
if a<10000:
    print("You have been warned")
else:
    print("enough balance")

Ans:11
a = int( input("what's the number:"))
if a%2==0:
    print("Even")
else:
    print("Odd")

Ans:12
a = int( input("what's the number:"))
b = int( input("what's the number:"))
if a>b:
    print("a is bigger")
else:
    print("b is bigger")

Ans:13
a = int( input("what's the number:"))
if a>18:
    print("elegible")
else:
    print("nope, you underage")

Ans:14
a = int( input("what's the marks:"))
if a>=40:
    print("pass")
else:
    print("fail")

Ans:15
a = int( input("what's the number:"))
if a<0:
    print("Negative")
else:
    print("Positive")

Ans:16
a = ("a","e","i","o","u","A","E","O","I","U")
b = input("what's the Alphabet:")
if b in a:
    print("vowel")
else:
    print("consonant")

Ans:17
a = int( input("what's the year:"))
if a==365:
    print("Leap year")
else:
    print("Not a leap year")

Ans:18
a = input("Type password:")
if a=="admin123":
    print("Valid Password")
else:
    print("Invalid Password")

Ans:19
a = int( input("Whats the salary:"))
if a>40000:
    print("Taxable")
else:
    print("Not Taxable")

Ans:20
a = int( input("what's the number:"))
if a>50:
    print("Greater than 50")
else:
    print("Smaller than 50")

Ans:21
a = int( input("what's the number:"))
b = int( input("what's the number:"))
c = int( input("what's the number:"))

if a>=b:
    if a>=c:
        print("A is Greater")
    else:
        print("C is Greater")
else:
    if b>=c:
        print("b is greater")
    else:
        print("c is greater")

Ans:22

a = int( input("what's the number:"))

if a>=0:
    if a>0:
        print("Positive")
    else:
        print("Zero")
else:
    print("Negative")

Ans:23

a = int( input("Whats the marks:"))

if a>=75:
    if a>=90:
        print("A")
    else:
        if a>=75:
            print("B")
        else:
            print("C")
else:
    if a<60:
        print("Fail")
    else:
        print("C")
            
Ans:24
a = int( input("what's the angle:"))
b = int( input("what's the angle:"))
c = int( input("what's the angle:"))

if a==b==c:
    if a==b==c:
        print("equilateral")
    else:
        print("scalene")
else:
    if a==b or a==c or b==c:
        print("isosceles")
    else:
        print("scalene")

Ans:25
a = input("What's the Character: ")

if a.isupper():
    print("Uppercase Letter")
else:
    if a.islower():
        print("Lowercase Letter")
    else:
        if a.isdigit():
            print("Digit")
        else:
            print("Special Character")

Ans:26
a = int( input("What's the Usage: "))

if a>=0:
    if a<=100:
        print(a*5)
    else:
        if a>101 and 1<=200:
            print((100*5)+(a-100)*10)
        else:
            if a>201 and a<=300:
                print((100*5)+(100*10)+(a-200)*15)
            else:
                print((100*5)+(100*10)+(100*15)+(a-300)*20)

Ans:27
a = input("What's the Username: ")

if a!=" ":
    if a=="Hula Girl":
        b = input("What's the Passcode: ")
    else:
        if b=="12345678":
            print("Hello,Hula girl")
        else:
            print("wrong password?")

Ans:28
a = int( input("Whats the marks of subject Z:"))
b = int( input("Whats the marks of subject X:"))
c = int( input("Whats the marks of subject Y:"))
d = a+b+c

if d>=0:
    if d>=270:
        print("A")
    else:
        if d>=225:
            print("B")
        else:
            print("C")
else:
    if d<180:
        print("Fail")
    else:
        print("C")

Ans:29
a = int( input("what's the number Z:"))
b = int( input("what's the number X:"))
c = int( input("what's the number Y:"))

if a>b and a<c or a<b and a>c:
    print("Z is Second")
else:
    if b>a and b<c or b<a and b>c:
        print("X is Second")
    else:
        print("Y is Second")

Ans:30
a = int( input("What's the age: "))

if a>=18:
    print("Elegiable age")
    b = int( input("What's the Salary: "))
    if b>=20000:
            print("Salary Elegiable")
            c = int( input("What's the Credit Score: "))
            if c>=400:
                print("Credit Score is good enough")
            else:
                print("Bad Credit score")
    else:
            print("Salary little, no offence")
else:
    print("Too young")

Ans:31
a = int( input("What's the day number: "))

if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thrusday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
elif a==7:
    print("Sunday")
else:
    print("Error")

Ans:32
a = int( input("What's the day number: "))

if a==1:
    print("January")
elif a==2:
    print("Febuary")
elif a==3:
    print("Marach")
elif a==4:
    print("April")
elif a==5:
    print("May")
elif a==6:
    print("June")
elif a==7:
    print("July")
elif a==8:
    print("Aguast")
elif a==9:
    print("September")
elif a==10:
    print("Octuber")
elif a==11:
    print("November")
elif a==12:
    print("December")
else:
    print("Error")

Ans:33
a = int( input("What's the Percentage: "))

if a>=90:
    print("A")
elif a>=75:
    print("B")
elif a>=60:
    print("C")
else:
    print("Fail")

Ans:34
a = int( input("What's the experience in years: "))

if a>=20:
    print("30%")
elif a>=10:
    print("20%")
elif a>=5:
    print("10%")
else:
    print("5%")

Ans:35
a = int( input("What's the Colour: "))

if a=="Red":
    print("Stop")
elif a=="Yellow":
    print("ready")
elif a=="Green":
    print("Go")
else:
    print("5%")

Ans:36
a = int( input("What's the experience in years: "))

if a<=20:
    print("Cold")
elif a>=21 and a<=30:
    print("Warm")
elif a>=31:
    print("Hot")
else:
    print("Error")

Ans:37
a = int( input("What's the Salary: "))

if a>=100000:
    print("Very High Earner")
elif a>=75000 and a<100000:
    print("High Earner")
elif a>=50000 and a<75000:
    print("Very Good Earner")
elif a>=25000 and a<50000:
    print("Good Earner")
elif a>=0 and a<25000:
    print("Entry Level")
else:
    print("Error Detected")

Ans:38
a = int( input("What's the Purchase Amount: "))

if a>=100000:
    print("25%")
elif a>=75000 and a<100000:
    print("20%")
elif a>=50000 and a<75000:
    print("15%")
elif a>=25000 and a<50000:
    print("10%")
elif a>=0 and a<25000:
    print("5%")
else:
    print("Error Detected")

Ans:39
a = int( input("What's the Number: "))

if a>=100:
    print("Three Digit")
elif a>=10 and a<100:
    print("Two Digit")
elif a>=0 and a<10:
    print("One Digit")
else:
    print("Error Detected")

Ans:40
a = int( input("What's the Numeber: "))
if a>=75:
    print("Excellent")
elif a>=50 and a<75:
    print("Good")
elif a>=25 and a<50:
    print("Average")
elif a>=0 and a<25:
    print("Poor")
else:
    print("Error Detected")

Ans:41
a = int( input("What's the Numeber: "))

if a%5==0 and a%11==0:
    print("Divisable by 5 and 11")
else:
    print("Not Divisable")

Ans:42
age = 21
salary = 25000
credit_score = 700

if age>=21 and salary>=25000 and credit_score>=700:
    print("Elegible")
else:
    print("Not Elegible")

Ans:43
username = "admin123"
passcode = "12345678"

if username=="admin123" and passcode=="12345678":
    print("Logged In")
else:
    print("Credentials Wrong")

Ans:44
math = 44
hindi = 100
english = 49

if math>=40 and hindi>=40 and english>=40:
    a = (math + hindi + english)/3
    if a>=50:
        print("Pass")
    else:
        print("Fail")

Ans:45
a = 23

if a>=10 and a<=100:
    print("number is between 10 and 100")
else:
    pritn("It doesn't exists")

Ans:46
a = int( input("What's the Number: "))
b = input("have any medical certificate available(Y/N):")

if a>=75 or b=="Y":
    print("Can give exams")
else:
    ("inelegible")

Ans: 47
a = int( input("What's the Day: "))
b = int( input("What's the Mounth: "))
c = int( input("What's the Year: "))
if a<1 or a>31:
    print("Invalid day")
    

else:
    if b<1 or b>12:
        print("Invalid Month")
       
    else:
        if c<1 or c>2026:
            print("Invalid Year")
        else:
            print("Date is Valid,","Your Date:",a,b,c)

Ans:48
a = input("Whats the email:")

if ("@")in a and (".") in a:
    print("Valid Email")
else:
    print("invalid")

Ans:49
a = int( input("What's the age:"))
b = input("What's the health status(good/avg/bad):")
c = int( input("What's the income:"))

if a>=18 and a<=70 and b=="good" or b=="avg" and c>=20000:
    print("Elegiable")
else:
    print("Inelegiable")

Ans:50
a = int( input("What's the year:"))

if a%400==0 or a%4==0 and not a%100==0:
    print("Leap year")
    if a%100==0 and not a%400==0:
        print("Not leap year")
else:
    print("Not leap year")

Ans:51
a = int( input("What's the salary:"))

if a<=500000:
    print("No Income Tax")
elif a>500000 and a<=1000000:
    print((a-500000)*5/100,"Income Tax of 5% on income more than 500000")
elif a>1000000 and a<=1500000:
    print("Income Tax of 5% on income more than 500000 adn 10% on income more than 1000000",((500000)*5/100)+((a-1000000)*10/100))
else:
    print("")

Ans:52
a = float( input("What's the Balance:"))
b = float( input("How much amount you want to withdraw:"))

if b<=0:
    print("Error Detected, must have put 0 or - bal")
elif b>a:
    print("You can't withdraw more than bal")
else:
    print("here your remaining balance:",a-b)

Ans:53
a = float( input("What's the Performance(out of 10):"))
b = float( input("How much Expirence:"))

if a>=7 and b>=10:
    print("Eleigable for promotion")
elif a>3 and b>=5:
    print("fast track to promotion")
else:
    print("Not Elegiable for promotion")

Ans:54
a = float( input("What's the marks:"))

if a>=90:
    print("Grade A")
    if a>=70 and a<90:
        print("Grade B")
        if a>=50 and a<70:
            print("Grade C")
            if a>=30 and a<50:
                print("Grade D")
else:
    print("Fail")

Ans:55

a = input("Write your password:")

if len(a)<=8:
    print("Length of the passowrd is too short")
elif a.lower()==a:
    print("Passoword dont consist upper case letter")
elif a.upper()==a:
    print("")
elif not any (char.isdigit() for char in a):
    print("Password should consist a number")
elif not any(char in "~!@$%^&*" for char in a):
    print("Passoword should cantain atleast one speacial character")

else:
    print("Valid passowrd")

Ans:56
a = input("What's the Location(Domestic,International as D and I):")
b = int (input("How much Order Amount:"))

if a=="D" and b<=5000:
    print("Delihvery Charges is 3% of amount")
elif a=="I" and b<=10000:
    print("Delhivery Charges is 7% of amount")
else:
    print("Free of Charges")

Ans:57
a = float( input("What's the Attendance:"))
b = float( input("Whats the Internal Marks:"))

if a>=75 and b>=40:
    print("Elegaible for examination")
else:
    print("Inelegaible")

Ans:58
a = int( input("What's the Age:"))
b =input("Whats the time(Day and Night as D and N):")

if a>=18 and b=="D":
    print("Cost the movie ticked is 300")
elif a>=18 and b=="N":
    print("Cost of the movie ticket is 500")
else:
    print("Inelegaiable to watch the movie")

Ans:59
a = float( input("What's the Balance:"))

if a>=10000000:
    print("Premium Account")
elif a>= 1000000 and a<10000000:
    print("Gold Account")
elif a>=100000 and a<1000000:
    print("Silver Account")
else:
    print("Base")

Ans:60
a = int(input("Whats the number:"))
b = int(input("Whats the number:"))

print(" A.Addition \n B.Subtraction \n C.Multiple \n D.Divison")
c = input("What you wanna do?")
if c == "A":
    print(a+b)
elif c == "B":
    print(a-b)
elif c == "C":
    print(a*b)
elif c == "D":
    print(a/b)
else:
    print("Error")

"""
























































































