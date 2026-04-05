""" Store Management System """

# Importing libraries 
import pickle
import os

# Adding a Method to add a customer  
def addcustomer():
    file =open('customer.bin','ab')
    cid = int(input("Enter customer ID:"))
    cname = input("Enter customer name:")
    cadd = input("Enter customer address:")
    cmobile = int(input("Enter customer mobile number"))
    pickle.dump(cid,file)
    pickle.dump(cname,file)
    pickle.dump(cadd,file)
    pickle.dump(cmobile,file)
    print("\n\t Customer Added Succesfully!!")
    file.close()
    input("Pres ENTER to Continue...")

#Adding a Method to View all customer

def viewallcustomers():
    file = open('customer.bin','rb')
    try:
        while True:
            for i in range(4):
                data = pickle.load(file)
                print('\t',data,end='')
            print()
    except:
        print("Here All The Customers!!")

#Adding a Method to delete a customer

def deletecustomer():
    file1 = open('customer.bin','rb')
    file2 = open('temp.bin','ab')
    flag1 = 0
    V1 = int(input("Which Customer to Delete,Enter their customer ID:"))

    try:
        while True:
            data = pickle.load(file1)
            if data==V1:
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                flag1 = 1
            else:
                pickle.dump(data,file2)

    except:
        if flag1==0:
            print("\n\tCustomer Not Found")
        else:
            print("Customer",V1,"Deleted Successfully")
    
    file1.close()
    file2.close()
    os.remove('customer.bin')
    os.rename('temp.bin','customer.bin')

def addproduct():
    file = open('product.bin','ab')
    pid = int(input("What be the product ID:"))
    pname = input("what be the product name:")
    pprice = int(input("Whats the product price:"))
    pickle.dump(pid,file)
    pickle.dump(pname,file)
    pickle.dump(pprice,file)
    print("Product Added")
    file.close()
    input("Press Enter to Continue...")


def viewallproduct():
    file = open('product.bin','rb')
    try:
            
        while True:
            print("\tProduct ID:",pickle.load(file))
            print("\tProduct Name:",pickle.load(file))
            print("\tProduct Price:",pickle.load(file))
            print("\t*****************************")
    except:
        print("Here all the products")

        
def updateproduct():
    file1 = open('product.bin','rb')
    file2 = open('temp.bin','ab')
    V1 = int(input("Whats the PID of the Product you want change price of:"))
    flag = 0
    
    try:
        while True:
            data = pickle.load(file1)
            if V1==data:
                pickle.dump(data,file2)
                
                name = pickle.load(file1)
                pickle.dump(name,file2)
                
                price = print("Old Price: ",pickle.load(file1))
                price = input("Whats the new price: ")
                pickle.dump(price,file2)
            else:
                pickle.dump(file2)
            flag = 1
    except:
        if flag==1:
            print("Price Updated Sucessfully")
        else:
            print("PID didnt found")

    file1.close()
    file2.close()
    os.remove('product.bin')
    os.rename('temp.bin','product.bin')


    
            
        





#Making the Program itself


while True:
    print("\n\n\t Store Management System")
    print('''


        1. Add Customer
        2. View All Customer
        3. Delete A Customer
        4. Add Product
        5. View All Products
        6. Update Product
        7. Place An Order
        8. View All Orders
        9. View All Orders By CID
        0. Exit

    ''')

    AskingWhatYouWannaDo = int(input("Enter what you wanna do:"))

    if AskingWhatYouWannaDo==0:
        break
        print("BYE-BYE ONI_CHAN")

    if AskingWhatYouWannaDo==1:
        addcustomer()
    if AskingWhatYouWannaDo==2:
        viewallcustomers()
    if AskingWhatYouWannaDo==3:
        deletecustomer()
    if AskingWhatYouWannaDo==4:
        addproduct()
    if AskingWhatYouWannaDo==5:
        viewallproduct()
    if AskingWhatYouWannaDo==6:
        updateproduct()

