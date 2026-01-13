List = ['boy','girl','a','b']
for eachItem in List:
    print(eachItem)
String = "words"
for eachWord in String:
    print(eachWord)
for item in range(10):
    print(item)
Dictionary = {'ban':80,'eng':84,'math':95}
for sub,marks in Dictionary.items():
    print("{}:{}".format(sub,marks))
Set = {1,2,3}
for uniqueNumber in Set:
    print(uniqueNumber)
for number in range(1,11):
    if number==6:
        continue
    print(number)

name = {'kotha','uma','usosi'}
index=0
while index<len(name):
    print(index)
    index +=1

word= "hello"
index=0
while index<len(word):
    print(word[index])
    index +=1

Selarys = {"A":8000,"B":10000,"C":11000}
keys=list(Selarys.keys())
index=0
while index<len(keys):
    eachKey=keys[index]
    selary="{}:{}".format(eachKey,Selarys[eachKey])
    print(selary)
    index +=1