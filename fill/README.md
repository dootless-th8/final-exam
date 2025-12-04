# oo_delivery.py

## Overview
This project is about creating a minimal proceess of delivery service in oop style. There are 4 classes Person, Customer, Driver, and DeliveryOrder. You can create people to order items around while assigning certain driver to the specific item. Each order will have a real time status to determin whether it has been delivered or not, which will change how in the summary method of the DeliveryOrder class will be printed out. 

## Features
* ### class Person:
       @Requires 1 argument
       Attribute: name(arg) 
       Method: 
            introduce(): Can return string Hi with the name

    #### Customer (Inherit Person):    
        @Requires 2 argument
        Contains: name(inherit Person)(arg), address(arg)
        Method: 
            place_order( item:str ): Can order thing which intern returns a DeliveryOrder object
        !!composit of DeliveryOrder

    #### Driver (Inherit Person):        
        @Requires 2 argument
        Contains: name(inherit Person)(arg), vehhicle(arg)
        Method: 
            deliver( order:DeliveryOrder ): Prints delivered text with and switchs DeliveryOrder obj's order status to "delivered"
        !!composit of DeliveryOrder

* ### class DeliveryOrder:
        has order info
        @Requires 2 argument
        Contains: customer(arg), item(arg), status
        Method: 
            assign_driver( driver:Driver ): Assign the driver to this order
            summary(): If the order hasn't been delivered, it will then list the info of the order(item, customer's name, status, driver's name).else it will just give out text "Order for ***Laptop*** → delivered"
        

## How to run
Create driver and customer objects first, then assigned the order of each customers. You can determined if the order has been delivered by running deliver out of the Driver object: it needs specific DeliveryOrder object as well. Furthermore, you can always check the status of the order by running summary from the certain DeliveryOrder object.

Please Enjoy

Examples:
```bash
alic = Customer("Alice", "Idaho")
print(alic.introduce())

bb = Customer("Bob", "Bannna")
print(bb.introduce())

dvd = Driver("David", "motorcycle")
print(dvd.introduce())

print()
# summ
or1 = alic.place_order("Laptop")
or1.assign_driver(dvd)
or2 = bb.place_order("Headphones")
or2.assign_driver(dvd)


print(or1.summary())
print(or2.summary())

dvd.deliver(or1)
dvd.deliver(or2)

print()

print(or1.summary())
print(or2.summary())

```

## Project Structure
```bash
|-fill
|   --oo_delivery.py    # The program
|   --README.md         #This file
|   --res.png           #Evidence
```

There's seems to be no bug