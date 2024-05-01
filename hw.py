"""
Exercise-1: Find missing elements
Write a function "missing_elements(my_list: list) -> list" that takes a
sorted list of integers and returns a list of missing integers in the range of the list.


"""
def missing_elements(my_list: list) -> list:
    missing = []
    for i in range(len(my_list) - 1):
        diff = my_list[i + 1] - my_list[i]
        if diff > 1:
            for j in range(1, diff):
                missing.append(my_list[i] + j)
    return missing

print(missing_elements([1, 2, 4, 6, 7]))  


"""
Exercise-2: Count occurrences
Write a function "count_occurrences(my_list: list) -> dict" that takes a
list of integers and returns a dictionary where keys are unique integers
from the list and values are their counts in the list.


"""
def count_occurrences(my_list: list) -> dict:
    occurrences = {}
    for num in my_list:
        occurrences[num] = occurrences.get(num, 0) + 1
    return occurrences

print(count_occurrences([1, 2, 3, 1, 2, 4, 5, 4]))  


"""
Exercise-4: Common elements
Write a function "common_elements(list1: list, list2: list) -> list" that takes two
lists of integers and returns a list of unique common elements.

"""
def common_elements(list1: list, list2: list) -> list:
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

print(common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))  # Output: [3, 4, 5]


"""
Exercise-5: Character frequency
Write a function "char_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each character in the string.

"""
def char_frequency(my_string: str) -> dict:
    frequency = {}
    for char in my_string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

print(char_frequency('hello world'))


"""
Exercise-6: Unique words
Write a function "unique_words(my_string: str) -> int" that takes a
string and returns the number of unique words in the string.

"""
def unique_words(my_string: str) -> int:
    words = my_string.split()
    return len(set(words))

print(unique_words('hello world hello'))  

"""
Exercise-7: Word frequency
Write a function "word_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each word in the string.

"""
def word_frequency(my_string: str) -> dict:
    words = my_string.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

print(word_frequency('hello world hello'))  


"""
Exercise-8: Count elements in range
Write a function "count_in_range(my_list: list, start: int, end: int) -> int" that
takes a list of integers and two integers as range boundaries and
returns the count of unique elements within that range in the list.


"""
def count_in_range(my_list: list, start: int, end: int) -> int:
    unique_elements = set(my_list)
    count = 0
    for num in unique_elements:
        if start <= num <= end:
            count += 1
    return count

print(count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4))


"""
Exercise-9: Swap dictionary keys and values
Write a function "swap_dict(d: dict) -> dict" that takes a dictionary
and returns a new dictionary where keys become values and values become keys.
if you face duplicates, the first key should be saved.


"""
def swap_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}

print(swap_dict({1: 'a', 2: 'b', 3: 'c'}))


"""
Exercise-10: Subset check
Write a function "is_subset(set1: set, set2: set) -> bool" that takes two
sets and returns True if set2 is a subset of set1, and False otherwise.


"""
def is_subset(set1: set, set2: set) -> bool:
    return set2.issubset(set1)

print(is_subset({1, 2, 3, 4, 5}, {3, 4, 5}))


"""
Exercise-11: Intersection of lists
Write a function "list_intersection(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in both lists.

"""
def list_intersection(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))

print(list_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))


"""
Exercise-12: Union of lists
Write a function "list_union(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in either of the lists.


"""
def list_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))

print(list_union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))


"""
Exercise-13: Most frequent element
Write a function "most_frequent(my_list: list) -> int" that takes a
list of integers and returns the most frequent element in the list.


"""
def most_frequent(my_list: list) -> int:
    return max(set(my_list), key=my_list.count)

print(most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]))


"""
Exercise-14: Least frequent element
Write a function "least_frequent(my_list: list) -> int" that takes a
list of integers and returns the least frequent element in the list.


"""
def least_frequent(my_list: list) -> int:
    return min(set(my_list), key=my_list.count)

print(least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]))


