Dic = {
    "name":"hasan",
    "age":26,
    "city":"dhaka"
}

print(Dic)
print(Dic['name'])
print(Dic.get('name'))

Dic.update({"name":"akhi"})
print(Dic)
print(Dic.values())
print(Dic.items())

Dic.pop("age")
print(Dic)