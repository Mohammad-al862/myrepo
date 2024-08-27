#

class Bank:
    def _init_(self,balance):
        self.balance = 0
        print("hello,welcome to the deposit & withdraw")

    def deposit(self):
        amount = float(input("enter amount for deposit:"))
        self.balance = amount
        print("\n amount deposited:",amount)

    def withdraw(self):
        amount = float(input("enter the amount for withdraw:"))
        if self.balance>=amount:
            self.balance-=amount
            print("\n you withdrew:",amount)
        else:
            print("\n insufficent balance")

    def display(self):
        print("\n net available balance=",self.balance)


s = Bank()
s.deposit()
s.withdraw()
s.display()


#

class ShoppingCart:
    def __init__(self):
        self.items =[]

    def add(self,item_name,qty):
        item = (item_name,qty)
        self.items.append(item)

    def remove(self,item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def caliculation(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
        
        
cart = ShoppingCart()
cart.add("papaya",100)
cart.add("mango",200)
cart.add("orange",150)
print("current items in cart:")
for item in cart.items:
    print(item[0],"_",item[1])

total_qty = cart.caliculation()
print('total quantity:" total_qty')

cart.remove("papaya")
print("\nupdated items in cart after removing papaya:")
for item in cart.items:
    print(item[0],"_",item[1])

total_qty = cart.caliculation()
print("total quantity:",total_qty)

            

