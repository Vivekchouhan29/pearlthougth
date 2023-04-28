from collections import Counter

arr = [1, 2, 3, 4, 2, 3, 4, 5, 6, 4, 3, 2, 1, 3, 4]

# count the frequency of each element in the array
count = Counter(arr)

# print the frequency of each element
for element, frequency in count.items():
    print(f"{element} appears {frequency} times in the array")