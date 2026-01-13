# list (ordered, mutable)

values = [0.51, 0.82, 0.91, 0.95]
values.append(0.41)

first_value = values[0]
last_value = values[-1]

total_epochs = len(values)

print("Values:", values)
print("First value", first_value)
print("Last value:", last_value)
print("Total epochs:", total_epochs)

print("\nValue per epochs: ")
for epoch, value in enumerate(values,start=1):
    print(f"Epoch{epoch}: Value{value}")

#tuple(ordered,immutable)

image_size = (224,224)
width=image_size[0]
height=image_size[1]
print("Width:", width)
print("Height:", height)

#set(unordered,unique)

animals = {"cat","bird","dog","cat"}
animals.add("tiger")
animals.discard("dog")
print("\nUnique Animals:",animals)

#dictionary(key-value mapping)

model_config = {
    "learning_rate": 0.02,
    "epochs": 50,
    "optimizer": "gost"

}
#access value
epochs = model_config.get("epochs")
#update value
model_config["epochs"]=100
#add new key-value pair
model_config["batch_size"]=30
print("\nModel configuration:")
for key, value in model_config.items():
    print(f"{key}:{value}")

#check if key exist

if "optimizer" in model_config:
    print("\noptimizer is exist")
