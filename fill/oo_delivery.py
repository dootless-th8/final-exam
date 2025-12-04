

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi {self.name}."
    





class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
    
    def place_order(self, item):
        return DeliveryOrder(self.name, item)        

class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle

    def deliver(self, order):
        print(f"{self.name} is delivering {order.item} to {order.customer} using {self.vehicle}.")
        order.status = "delivered"


class DeliveryOrder:
    def __init__(self, customer, item):
        self.customer = customer
        self.item = item
        self.status = "preparing"
    
    def assign_driver(self, driver):
        self.driver = driver
        pass
    def summary(self):
        if self.status == "preparing":
            return (f"Order Summary:\n"
                    f"Item: {self.item}\n"
                    f"Customer: {self.customer}\n"
                    f"Status: {self.status}\n"
                    f"Driver: {self.driver.name}\n"
                    )
        elif self.status == "delivered":
            return f"Order for {self.item} → delivered"
        

# main
# hi
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

print("Final Status:")
print(or1.summary())
print(or2.summary())
