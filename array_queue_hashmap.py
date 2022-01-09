# coding part of arrays , stacks, ques, hashmap

# arrays : collection of similar data types - homogenous

# store the marks of 5 students = 100, 80, 79, 90
array = [100, 80, 79, 90]

# marks of 4th student
print("Marks of the 4th student is :", array[3])
array[3] += 10

print(array)

# stack - push , pop , peek
"""
book5
book4
book3
book2
book1
"""
# push is pushing on top of stack- stack.append("book1
stack = ["book 100", "book2", "book311", "book40", "book5", "book1", "book1"]

if len(stack) > 5:
    print("Stack overflow")
else:
    print("It's okay")

stack = ["book2", "book100"]

# peek
print()
print("The topmost book is ", stack[-1])
print("After peek, my stack is ", stack)

# pop
print()
print("The topmost book is ", stack[-1])
stack.pop()
print("After pop, my stack is ", stack)

# queue

queue = ["p1", "p2", "p3", "p4", "p5", "p6"]
# enqueue - enter
print("After person 6 comes in, my queue is :", queue)

m = int(input("Enter how many people left the queue/ have completed withdrawing the money from ATM "))
print("My new queue after", m, " people left is ", queue[m:])
print(queue)

for i in range(m):
    queue.pop(1)
print(queue)

# strings manipulation

email = ["abc@gmail.com", "arrav@gmail.com", "riya@gmail.com"]
for values in email:
    name = values.split("@")[0]
    print(name)
    print()

# hashmaps

hashmap = {1001: ["ab", 45], 102: ["av", 56], 1002: ["gh", 67, 78], 101: "zz"}
print(hashmap)
print()

# we want to add one key: value pair
hashmap[34] = "neuron"
print("new hashmap is: ", hashmap)
print("The value for the key is 102 is: ", hashmap.get(102))

for key in hashmap:
    print(key, "-->", hashmap[key])
    print()

# frequency hashmap

arr = [1, 2, 2, 2, 2, 33, 3, 3, ]
hm = {}
for number in arr:
    if number not in hm:
        hm[number] = 1
    else:
        hm[number] += 1
print(hm)

# counter

from collections import Counter
c = Counter(arr)
print(c)

