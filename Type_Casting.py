#type casting = convert the data type of a value to another data type.

#int
x = 1
#float
y = 2.0
#str
z = "3"

print(x)
print(y)
print(z)

#convert float to int
print(int(y))
y = int(y)
print(y)

#convert str to int
print(z*3)
z = int(z)
print(z*3)

#convert int to float
x=float(x)
print(x)

#example
#print("X is "+x)
#TypeError: can only concatenate str (not "float") to str
print("X is "+str(x))
