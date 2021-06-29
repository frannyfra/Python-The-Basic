
# This is our first Python Script;
# This is a comment!

print("Hello world!!!")

# Indentation:
x = 1
if x > 0:
    print("x is greater than zero")
else:
    print("x is less than zero")

# Variables and Data Types:

age = 18
print(type(age))
# Will print <class "int> - same as typeof in JS

name = "Francesca"
# "" or '' are delimeter in python; 
print(type(name), name)

# Casting -> it returns a floating even though the number is an integer - converstion in JS?
number = float(2)
print(type(number))

# Tuple 
number_and_age = (number, age)
print(number_and_age)
