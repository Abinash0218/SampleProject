class Bank:
    def __init__(self):
      self.__balance=1000  # private

    def deposit(self,amount):
       self.__balance+=amount

    def show(self):
       print(self.__balance)

b=Bank()
b.deposit(2000)
b.show()


class Person:
   def __init__(self,name):
      self.__name=name

   def get_name(self):
      return self.__name
   
   def set_name(self,name):
      self.__name=name

p=Person("Abi")
print(p.get_name())
p.set_name("Ajay")
print(p.get_name())
