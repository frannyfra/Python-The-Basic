# Tuple cannot be changed is not mutable 
# IT DOES keep the position

tuple_a = ("Cat", "Dog", "Mouse")
print(tuple_a)

# tuple_a.append("Lopa")
# print(tuple_a)
#Traceback (most recent call last):
# File "tuple.py", line 7, in <module>
# tuple_a.append("Lopa")
# AttributeError: 'set' object has no attribute 'append'


print(tuple_a[0])
print(tuple_a[1])
print(tuple_a[2])
