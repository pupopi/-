#Chapter21

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
print(stack.is_empty())


stack = Stack()
stack.push(1)
print(stack.is_empty())


stack = Stack()
stack.push(1)
item = stack.pop()
print(item)
print(stack.is_empty())


stack = Stack()

for i in range(0, 6):
    stack.push(i)

print(stack.peek())
print(stack.size())


###

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
for c in "Hello":
    stack.push(c)

reverse = ""

while stack.size():
    reverse += stack.pop()

print(reverse)


#キュー

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


a_queue = Queue()
print(a_queue.is_empty())


a_queue = Queue()

for i in range(5):
    a_queue.enqueue(i)

print(a_queue.size())


a_queue = Queue()

for i in range(5):
    a_queue.enqueue(i)

while a_queue.size():
    print(a_queue.dequeue())

print()
print(a_queue.size())


#ticket

import time
import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def simulate_line(till_show, max_time):
    pq = Queue()
    tix_sold = []

    for i in range(100):
        pq.enqueue("person" + str(1))

    t_end = time.time() + till_show
    now = time.time()
    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint((), max_time)
        time.sleep(r)
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)
        return tix_sold

    sold = simulate_line(5, 1)
    print(sold)