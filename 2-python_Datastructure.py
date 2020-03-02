from collections import deque  # for FIFO
items = [
    ("product", 10),
    ("product", 11),
    ("product", 13)
]
prices = list(map(lambda item: item[1], items))
priceFilter = filter(lambda item: item[1] > 10, items)
print(prices)
print(priceFilter)

# list comprehesion map
mapComprehesion = [item[1] for item in items]
print(mapComprehesion)
# list comprehesion filter
filterComprehesion = [item for item in items if item[1] > 10]
print('filterComprehesion', filterComprehesion)

# zip combine list
list1 = [1, 2, 3]
list2 = [10, 20, 30]

combineList = zip(list1, list2)
print('combineList', combineList)

# stack data structure
# LIFO (last in first out)

browsering_session = []
browsering_session.append(1)
browsering_session.append(2)
print("append session", browsering_session)

browsering_session.pop()  # remove last index
print('remove the session', browsering_session)
if not browsering_session:  # check to see if there is any more session left
    browsering_session[-1]
print("last session", browsering_session)

# FIFO (first in first out)
queue = deque([])
queue.append('1')
queue.append('2')
queue.append('3')
print(queue)
queue.popleft()  # remove first out
print(queue)
