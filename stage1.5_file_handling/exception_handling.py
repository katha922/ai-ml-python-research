try:
    with open('error.text','r') as file:
        content=file.read()
        result=10/int(content)
        print(result)

except Exception as e:
    print(e)

try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print(ZeroDivisionError)
finally:
    print("execution completed")