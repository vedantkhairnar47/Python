# List

# Syntax : []
# Heter
# Ordered
# indexed
# data mutable
# list mutable
# duplicate allowed

data = [10,90.67,"Hello",40,True]

print("datatype is : ",type(data))
print("length is : ",len(data))
print(data)

print(data[0])
print(data[1])
print(data[2])
print(data[3])

data[0] = 11
print(data[0])

data.append(40)
print(data[4])

print("Data display using loop")
for value in data:
    print(value)