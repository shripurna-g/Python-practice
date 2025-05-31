


'''
Goal: Write a function that takes a list of numbers and:
Removes duplicates
Sorts them in descending order
Returns both the original count and the final list
'''

def dedup_sort(input_list):

    count = len(input_list)
    dedup_list = list(set(input_list))
    dedup_list.sort(reverse=True)

    return input_list, dedup_list

if __name__ == '__main__':

    data = [5,9,2,8,0,4]

    count, cleaned = dedup_sort(data)

    print("Original count:", count)
    print("Cleaned list:", cleaned)


