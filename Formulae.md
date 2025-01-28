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










