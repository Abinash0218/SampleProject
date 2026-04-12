def greet():
    print("Hello World!")
greet()
greet()
greet()

def greet(name="guest"):
    print("Hello",name)
greet("Abinash")
greet()

def add(a,b=5):
    return a+b
result=add(10)
print(result)

def student(name, age):
    print(name,age)
student(age=20,name="Abinash")

def operations(a,b):
    return a+b, a-b, a*b, a/b, a%b

add,diff,mul,div,mod=operations(4,2)
print("sum=",add)
print("diff=",diff)
print("mul=",mul)
print("div=",div)
print("mod=",mod)

# *args
def total(*numbers):
    return sum(numbers)
print(total(1,2,3,4,5,6,7,8,9,10))

# **kwargs
def info(**data):
    print(data)
info(name="Abi",age=21,place="Hosur")

def function(*args,**kwargs):
    print("args:",args)
    print("kwargs:",kwargs)
function(10,20,30,name="Gowsick",age=20,place="Salem")    

# lambda function
add=lambda a,b: a+b
print(add(2,6))

x=10  # global scope
def test():
    y=5  # local scope


    