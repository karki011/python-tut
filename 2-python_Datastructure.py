# from collections import deque  # for FIFO
# items = [
#     ("product", 10),
#     ("product", 11),
#     ("product", 13)
# ]
# prices = list(map(lambda item: item[1], items))
# priceFilter = filter(lambda item: item[1] > 10, items)
# print(prices)
# print(priceFilter)

# # list comprehesion map
# # [experssion for item in items]
# mapComprehesion = [item[1] for item in items]
# print(mapComprehesion)
# # list comprehesion filter
# filterComprehesion = [item for item in items if item[1] > 10]
# print('filterComprehesion', filterComprehesion)

# # zip combine list
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# combineList = zip(list1, list2)
# print('combineList', combineList)

# # stack data structure
# # LIFO (last in first out)

# browsering_session = []
# browsering_session.append(1)
# browsering_session.append(2)
# print("append session", browsering_session)

# browsering_session.pop()  # remove last index
# print('remove the session', browsering_session)
# if not browsering_session:  # check to see if there is any more session left
#     browsering_session[-1]
# print("last session", browsering_session)

# # FIFO (first in first out)
# queue = deque([])
# queue.append('1')
# queue.append('2')
# queue.append('3')
# print(queue)
# queue.popleft()  # remove first out
# print(queue)
# if not queue:
#     print("queue is empty")

# # Tuples - read only list
# # point = ()  # empty tuples
# point = (1, 2)
# print(point)

# # swapping variable
# x = 19
# y = 11

# y, x = x, y
# print(x)
# print(y)

# # Arrays

# # sets- collection with no duplicates
# # cannot access using index use list
# numbers = [1, 1, 2, 2, 2, 3, 3, 4]
# first = set(numbers)
# second = {1, 2, 5}

# print('union', first | second)
# print('intersection', first & second)
# print('difference', first - second)

# # dictionaries - collection of key value pairs

# point = dict(x=1, y=2)
# print('dict', point)
# point["x"] = 12
# print('dict', point)
# point["z"] = 24
# print('dict', point)
# # to check key value pairs exitense
# print(point.get('z', 0))
# del point['z']
# print('dict', point)
# # loop over dict
# for key, value in point.items():
#     print(key, value)

# # generator expression - good for large number of data set
# values = (x * 2 for x in range(10))
# print(values)

# # unpacking iterable using *
# first = {"x": 1}
# second = {"x": 2, "y": 3}
# combined = {**first, **second, 'z': 45}
# print("unpacking dict", combined)

# # excerise
# # find most repearted character in the sentence
import re
a = "Wklv lv d vhfuhw phvvdjh"


def letter_frequency(text):
    s = re.sub(r"[^\w\s]", '', text.lower())
    print(s)
    newText = s.replace(' ', '')
    print('newText', newText)
    sortedText = sorted(newText)
    # print('sorted', sortedText)
    # create empty dict
    char_frequency = {}
    for char in sortedText:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    print(type(char_frequency))
    sorted_frequency = sorted(char_frequency.items(
    ), key=lambda key: key[1], reverse=True)
    print((sorted_frequency))
    print(type(sorted_frequency))

    return sorted_frequency


letter_frequency(a)
