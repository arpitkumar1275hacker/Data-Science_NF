# Write a program to create a dictionary from two lists

keys = ["name", "age", "city"]
values = ["Arpit", 21, "Noida"]

dictionary = dict(zip(keys, values))

print("Dictionary:", dictionary)


# Write a program to merge two dictionaries

dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

merged_dict = {**dict1, **dict2}

print("Merged Dictionary:", merged_dict)


# Write a program to sort a dictionary by its values

dict1 = {"a": 50, "b": 20, "c": 10, "d": 40}

sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1]))

print("Sorted Dictionary:", sorted_dict)



# Write a program to check if one set is a subset of another

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")

# Write a program to check whether two lists have a common element

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 3, 8, 9]

common = set(list1) & set(list2)

if common:
    print("Lists have common element(s):", common)
else:
    print("No common elements")
