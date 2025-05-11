# Array

## Array manipulation

from lists
numpy arrays vs array module arrays

## Creation

1d_array = np.array([1,2,3,4,5])
2d_array = np.array([1,2,3,4],[5,6,7,8])
3d_array = np.array([1,2],[3,4],[5,6])

## Initialisation

arr_zeroes = np.zeroes((3,3))
arr_ones = np.ones((2,4))
arr_range = np.arange((0,10,2))
arr_linspace = np.linspace(0, 1, 5)

## Indexing

arr = np.array([10, 20, 30, 40, 50, 50])

print(arr[2]) #30
print(arr[-1]) #50

arr_2d = np.array([1,2,3],[4,5,6],[7,8,9])

print(arr_2d[1,2]) #6
print(arr_2d[0,:]) #1,2,3

## Slicing

arr_2d = np.array([1,2,3],[4,5,6],[7,8,9])

subarr = arr_2d[0:2, 1:3] #2,3,5,6

## Arithmetic Ops

arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])

add = arr_1 + arr_2 #[5,7,9]
sub = arr_1 - arr_2 #[-3,-3,-3]
mul = arr_1 * arr_2 #[4,10,18]
div = arr_1 / arr_2 #[0.25, 0.4, 0.5]
scalar = arr*2

## Manipulation - shape, reshape

arr = np.array([1,2,3,4,5,6])

arr_reshaped = arr.reshape(2,3) #[1,2,3],[4,5,6]

arr_flat = arr_reshaped.flatten() #[1,2,3,4,5,6]

## Broadcasting - automatic adjustment of array shapes during element wise ops

arr_2d = np.array([1,2],[3,4])
arr_1d = np.array([10,20])

result = arr_1d + arr_2d #[11,22],[13,24]

## Aggregation

arr = np.array([1,2,3,4,5])

sum = arr.sum()
mean = arr.mean()
max = arr.max()
min = arr.min()
std = arr.std()

## Stacking

arr_1 = np.array([1,2])
arr_2 = np.array([3,4])

vertical = np.vstack((arr_1, arr_2)) #[[1,2]
                                       [3,4]]

horizontal = np.hstack((arr_1, arr_2)) #[1,2,3,4]

## Splitting

arr = np.array([1,2,3,4,5,6])

split_arr = np.array_split(arr,2) #array([1,2,3]), array([4,5,6])

## Masking - filter elements

arr = np.array([1,2,3,4,5])

mask = arr > 2

print(mask)

## Sorting

sorted_arr = np.sort(arr)

## Sorting with indices

sorted_indices = np.argsort(arr) #[1 3 0 2 4] - indices that would sort the array



# IO

user_input = input("Please enter something")

input = int(input("Enter number"))

height = float(input("Enter height"))

fruits = input("Enter CSV").split(",")

tuple_input = tuple(map(int, input("Enter").split(",")))

dict_input: key, value = input().split(",")

Input with default value: Name = input("Enter") or "John"


# File handling

with open("input.txt", r) as file:



# JSON handling

import json

json_input = input("Enter")
parsed_data = json.loads(json_input)



# Lists <-> Vector

Not hashable

## Initialisation

list = []
list = [1,2,3,4]
list = [1, "hello", 3.14, True]
list = [0]*5
list = range()
list = [for x in range(5)]

## List methods

len(my_list)
not(my_list)
my_list.reverse()
my_list.sort(reverse=True)
sorted(my_list)
my_list.append(4)
my_list.insert(1, "hello")
del(my_list[2]) OR my_list.remove()
for x in my_list:

# Dict <-> unordered_map

dict = {}
dict = {"name":"Alice", "age":25, "city":"NY"}
dict = dict(name = "Alice", age=25, city="Y")
dict = dict([("Name", "Alice"),("Age", 25),("City", "NY")])
dict = dict.fromkeys(["a", "b", "c"],0)
dict = {x**2 for x in range(5)}

e.g. dict = {"name":"Alice", "age":25, "city":"NY"}

Adding new key-value pair: my_dict["city"] = "NY"
Delete key-value pair: del my_dict["age"]
Key in dict: Print("name" in my_dict)
len(my_dict)
for key, value in dict.items()
for key in dict
dict.get(key, default_value)

## create dict with key being list of elements, values being default 
make unique: list(dict.fromkeys(my_list))

## dict comprehension
create dict by specfying key-value pairs

__{key_expression: value_expression for item in iterable if condition}__

squares = {x:x**2 for x in range(5)}
squares = {x:x**2 for x in range(5) if x%2==0}


## 2 lists (key list, value list)
dict = {keys[i]: values[i] for i in range(len(keys))}

## Invert keys and values
inverted = {v:k for k,v in original.items()}

## Nested comprehension
matrix = {i:{j:j*j for j in range(5)}} 

## Zip
keys = [,,]
values = [,,]

dict = {k:v for k,v in zip(keys, values)}

## Map
map(function, iterable) #apply function to each element in iterable
e.g., squares_map = list(map(lambda x:x**2, numbers))
uppercase = list(map(str.upper,words))

## Filter
filter(function, iterable)
e.g., even = list(filter(lambda x:x%2==0, numbers))

## Map + Filter
numbers = {1,2,3,4,5}
e.g., result = list(map(lambda x:x**2, filter(lambda x:x%2 == 0, numbers)))

# String

1. s.find(substring, start=0, end=len())
2. s.lower()
3. s.upper()
4. result = s.strip() #returns new string
5. s.replace(old, new)
6. s.split(",")
7. result = ",".join(iterable)
8. s.count("a")
9. s.startswith("he")
10. s.endswith("he")
11. s.isdigit()
12. s.isalpha()
13. s.isalnum()

# Set

Cannot contain mutable elements like lists or dicts

my_set = set()
my_set = (1,2,3,4)

1. set.add(element)
2. set.remove(element)
3. set.discard(element)
4. set1.union(set2) OR set1 | set2
5. set1.intersection(set2) OR set1 & set2
6. set1.difference(set2) OR set1 - set2
7. set1.symmetric_difference(set2) OR set1^set2
8. subset_check = set1.issubset(set2)
9. superset_check = set1.isuperset(set2)
10. set1.isdisjoint(set2)
    
# Tuples
immutable, hashable

my_tuple = (1,2,3)

tuple.count()

# Type Conversion

int(string)
str(int_value)
type(value)

# Removing duplcates

## order not preserved
list(set(my_list))

## order preserved

list(dict.fromkeys(my_list))

## DF

1. dh.head()
2. df.tail()
3. df.shape()
4. df.info()
5. df.describe()
6. df.columns()
7. df['Column_name']
8. df[['Col1',, 'Col2']]
9. df.iloc[]
10. df.loc[]
11. df.at[]
12. df.iat[]
13. df.dropna()
14. df.fillna()
15. df.replace()
16. df.drop()
17. df.rename()
18. df.astype()
19. df.sort_values()
20. df.sort_index()
21. df.groupby()
22. df.agg()
23. df.pivot_table()
24. df.crosstab()
25. df.merge()
26. df.join()
27. df.drop_duplicates(subset=['A'])
28. df[df['Column']>value]
29. df['Column'].str.contains()
30. df['Column'].isin()
31. df.apply(lambda x:condition, axis=1)


# Pandas

1. pd.DataFrame()
2. pd.read_csv()
3. pd.read_excel()
4. pd.concat()


# Numpy

1. np.array()
2. np.zeros()
3. np.ones()
4. np.arange()
5. np.linspace()
6. np.random.randn()
7. np.reshape()
8. np.transpose()
9. np.flatten()
10. np.split()
11. np.sum()
12. np.mean()
13. np.median()
14. np.std()
15. np.min()
16. np.max()
17. np.argmin()
18. np.argmax()
19. np.dot()
20. np.sqrt()
21. np.linalg.inv()
22. np.linalg.eig()
23. np.linalg.det()
24. np.linalg.solve()
25. np.corrcoef()
26. np.var()
27. np.percentile()






























































