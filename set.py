# Set are mutable
# Is not ordered
# Only contains unique values 

set_a = {1,2,3}
print(set_a)

set_a.add("four")
print(set_a)

set_a.update(["Five", "Six", "Seven"])
print(set_a)

set_a.add("Ten")
print(set_a, "after ten added")

# Discard and Remove
# return null remove returns an error

f_set_a = frozenset(set_a)
print(set_a)

set_a.add("ten")
print(set_a, "after frozing")
# does not throw error but it does not add neither