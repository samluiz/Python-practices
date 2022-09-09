import random

list1 = []
list2 = []

for x in range(10):
  list1.append(random.randrange(20))
  list2.append(random.randrange(10))

print(list1, list2)

for num in list1:
    if num in list2:
      print(f"The number {num} is in both lists.")