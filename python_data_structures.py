### LISTS ###
my_list = [1,2,3,4,5]
my_second_list = ['a','b','c','d','e']

# indexing and slicing
my_list[0:2]
my_list[-1]

# lists are mutable
my_list[3] = 18

# concatenation of two lists
my_third_list = my_list + my_second_list

# create list using range function
range_list = list(range(5))

# or
range_list = list(range(5,10))


# LIST METHODS

# list.append(x): add and item to the end of the lists
my_list.append(10)

# list.extend(iterable): extend the list by appending all the items from the iterable
my_list.extend(range(5))

# list.insert(i,x): insert an item at a given position. The first argument is the index of
# the element before which to insert
my_list.insert(0,10)

# list.remove(x): Remove the first item from the list whose value is equal to x
my_list.remove(10)

# list.pop([i]): Remove the item at a given position in the list and return it.
my_list.pop(2)

# list.clear(): remove all items from the list
my_third_list.clear()


# list.index(x[,start[,end]]): Return zero-based index in the list of the first item whose value is equal to x
my_list.index(3)

# list.count(x): returns the number of times x appears in the list
my_list.count(2)


# list.sort(*,key = None, reverse = False): Sort the items of the list in place
my_list.sort(reverse = True)

# list.reverse(): reverse the elements of the list in place
my_second_list.reverse()

# list.copy: return a shallow copy of the list
my_list.copy()


## LIST COMPREHENSIONS

squares = list(map(lambda x: x**2,range(10)))

squares = [x**2 for x in range(10)]

[(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

# Nested list comprehensions
matrix = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]

transposed_matrix = [[row[i] for row in matrix] for i in range(4)]

### TUPLES AND SEQUENCES ###

# A tuple consists of a number of values separated by commas
# Tuples can not be nested
# Tuples are immutable, but they can containt mutable objects
# Tuples can be input with or without surrounding parentheses
my_tuple = 12345, 54321, 'hello!'
print(my_tuple)
print(my_tuple[0])

v = ([1,2,3],[3,2,1])


### SETS ###
# A set is an unordered collections with no duplicate elements
# Curly braces or the set() function can be used to create sets

basket = {'apple','orange','apple','pear','orange','banana'}
print(basket)

a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)
print(a-b)
print(a|b)
print(a  & b)


### DICTIONARIES ###
# Unlike sequences (list,tuples and ranges) dictinaries are indexed by keys, which can be
# any immutable type; strings and numbers can always be keys.
# It is best to think of a dictionary as a set of key: value pairs, with the requirement that the
# keys are unique (within one dictionary). 
# A pair of of brace {} creates an empty dictionary
# Placing a comma separated lists of key:value pairs within the braces adds initial key:value pairs
# to the dictionary.


tel = {'jack':4098, 'sape': 4139}

tel['guido'] = 4127

print(tel)

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dict([('sape',4139),('guido',4127),('jack',4098)])

{x:x**2 for x in (2,4,6)}

dict(sape = 4139,guido = 4127,jack = 4098)


# Looping techniques
