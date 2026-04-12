class details:
    def __init__(self,name,age,country):
        self.name=name  # instance variable
        self.age=age
        self.country=country

    def greet(self):
        print("Hello",self.name)

    def intro(self):
        print(f"Hi I am {self.name}, {self.age} years old and I am from {self.country}")

    def greeting(self):
        print(f"Hi {self.name} welcome to India")

d1=details("Abi",20,"India")
d2=details("Ajay",21,"India")
d3=details("Arun",22,"Japan")
d1.greet()
d1.intro()
d2.greet()
d2.intro()
d3.greeting()
        