from datetime import datetime
itemname=[]
quan=[]
price=[]

while True :
    New_Customer=input("Go to next person?(Y/y/N/n): ")
    total=0
    totalamt=0
    if New_Customer=='n' or New_Customer=='N':
        break
    elif New_Customer=='y' or New_Customer=='Y':
        itemname.clear()
        quan.clear()
        price.clear()
        Customer_name=input("Enter Customer's name: ")
        while True:
            nameofprod=input("Enter the Name of item: ")
            quantity=int(input("Enter the quantity of item: "))
            items=int(input("Enter the price of items: "))
            total=quantity*items
            totalamt+=total
            itemname.append(nameofprod)
            quan.append(quantity)
            price.append(total)
            repeat =input("Do you want to repeat this process(Y/y/N/n): ")
            if repeat=='n' or repeat=='N':
                print("\n")
                print(25*"=",'Supermarket',25*"=")
                print(30*" ","store")
                print("Name:",Customer_name,30*" ","Date:",datetime.now())
                print(75*"-")
                print('items',8*" ","quantity",3*" ",'price')
                for i in range(len(itemname)):
                    print(itemname[i],10*' ',quan[i],10*" ",price[i])
                print(75*"-")
                print(50*" ",'TotalAmount:','Rs',totalamt)
                print(75*"-")
                print(25 *" ","Thanks for visting")
                print(75 *"")
                break
            elif repeat=='y' or repeat=='Y':
                print("Next Item!!!")
            else:
                print("Wrong input!! Try again!!")