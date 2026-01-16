#create
with open("create.text","w") as file:
    print("created")
    file.write("hello") #write

#read
with open("create.text","r") as file:
    content = file.read()
    print(content)