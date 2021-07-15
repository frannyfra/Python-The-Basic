
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

# List, Tuple, Dictionary, Frozenset, Set 
# ALL OF THE ABOVE Consent to store multiple values in a variable
# Datatypes are mutable or immutable

our_list = ["a", "b", "c", "d" , 18]
print(our_list)
# Array in JS? 
# Pass multiple values and keep the ordering of the values in the list 
# Pass multiple datatypes (like arrays in JS)


our_tuple = ("a", "b", "c")
# It is unmutable
print(our_tuple)

our_dictionary = {"name" : "francesca", "surname" : "Gallo"}
print(our_dictionary)

our_set = {"one", "two", "three"}
print(our_set)
# The difference between set and list is that set does not keep the position and element are unique

our_frozenset = frozenset(our_set)
print(our_frozenset) 
# It is the same as a set (like a set is the same as a list) but it cannot be changed 


