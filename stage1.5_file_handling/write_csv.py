import csv

data = [
    ["Name", "Salary", "Designation", "Department", "Location"],
    ["Alice", 70000, "Software Engineer", "IT", "New York"],
    ["Bob", 85000, "Data Scientist", "Data", "San Francisco"],
    ["Charlie", 60000, "System Administrator", "IT", "Chicago"],
    ["David", 95000, "Product Manager", "Product", "Boston"],
    ["Eve", 72000, "UX Designer", "Design", "Los Angeles"]
]

with open('new.csv','w') as file:
    csv_file= csv.writer(file)
    csv_file.writerows(data)
    print("created")