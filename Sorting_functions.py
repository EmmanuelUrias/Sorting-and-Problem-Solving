# Sort an unsorted numerical list

def sort_list(lst):
    lst.sort()
    return lst


list = [2, 5, 6, 3, 7, 8, 1]

# list.sort()

print(sort_list(list))
# print(list)

# Create a new sorted list from an unsorted list

unsorted = [2, 5, 6, 3, 7, 9, 1]

new_list = sorted(unsorted)
print(new_list)

# Algorithm to sort in descending order

descending_list = sorted(unsorted, reverse=True)
print(descending_list)


# def descending_sort(lst):
#     descending = sorted(lst, reverse=True)
#     print(descending)


# descending_sort(unsorted)
