# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/22
price = {"Banana": 4, "Apple": 2, "Orange": 1.5, "Pear": 3}
quantity = {"Banana": 1, "Apple": 0, "Orange": 3, "Pear": 2}
sum = 0
for i in price:
    sum += price[i] * quantity[i]
print("Total cost:", sum)



class fruit:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def sum(self):
        return self.price * self.quantity
    def print_answer(self):
        print(self.name, self.price, self.quantity, self.sum())


banana = fruit("Banana", 4, 1)
apple = fruit("Apple", 2, 0)  
orange = fruit("Orange", 1.5, 3)
pear = fruit("Pear", 3, 2)

sum = banana.sum() + apple.sum() + orange.sum() + pear.sum()
print("Total cost:", sum)