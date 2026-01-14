Set = {"unOrdered","unique","mutable","dynamicSize"}
Set.add(1)
Set.remove("unique")
Set.update(["heterogeneous"])
print(Set)

Set1 = {1,2,3}
Set2 = {4,5,6,2}

result = Set1.union(Set2)
result2 = Set1.intersection(Set2)
result3 = Set1.difference(Set2)
result4 = Set1.issubset(Set2)
print(result)
print(result2)
print(result3)
print(result4)