import random
print(random.random())
print(random.randint(000000,999999))  # to generate the otp randomly syntax: randint(start,stop)->it includes the stop value
print(random.randrange(111,999,3))  # example(111,114,117,120,...,996) syntax: randrange(start,stop,step)->it not inclues the stop value like 999-1=998
fruits=["Apple","Banana","Orange","Grapes"]
print(random.choice(fruits))
print(random.sample(fruits,2))
l=[1,2,3,4,5,6]
random.shuffle(l)
print(l)



from datetime import date, timedelta
today=date.today()
tomorrow=today + timedelta(days=1)
yesterday=today - timedelta(days=1)
print(tomorrow)
print(today)
print(yesterday)
print(today.year)
print(today.month)
print(today.day)# to get the date
print(today.weekday())# 0-6  0->Monday,..., 6->Sunday