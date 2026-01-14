def sum(a=0,b=0):
    print(a+b)
sum(1,2)

def touple(*numbers):
    print(numbers)
    for number in numbers:
        print(number)
touple(1,2,3,4)

def dic(**person):
    print(person)
    print(person['age'])

dic(
    name="akhi",
    age=25
)

result = lambda x,y: x+y
print(result(10,2))

def local():
    x=10
    y=20
    print(x+y)
local()