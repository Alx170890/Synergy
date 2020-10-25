# Реализация стека через однонаправленный список
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        if self.next:
            return f'{self.value} -> {self.next.value}'
        return f'{self.value} -> None'


class Stack:
    def __init__(self):
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def empty(self):
        return self.size == 0

    def put(self, value):
        self.root = Node(value, self.root)
        self.size += 1

    def get(self):
        if self.root is None:
            return None
        value = self.root.value
        self.root = self.root.next
        self.size -= 1
        return value


stacklist = Stack()
stacklist.put("1")
stacklist.put("2")
stacklist.put("3")
while not stacklist.empty():
    print(stacklist.get())

# Реализация очереди через однонаправленный список
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def add(self, newelem):
        newnode = Node(newelem)
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode

    def print(self):
        value = self.head
        while value is not None:
            print(value.value)
            value = value.next


list = SLinkedList()
list.head = Node("1")
list.head.next = Node("2")
list.add("3")
list.print()

# Функция для переворота односвязного списка
def is_right_math(equation):
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            if self.next:
                return f'{self.value} -> {self.next.value}'
            return f'{self.value} -> None'

    class Stack:
        def __init__(self):
            self.root = None
            self.size = 0

        def size(self):
            return self.size

        def empty(self):
            return self.size == 0

        def put(self, value):
            self.root = Node(value, self.root)
            self.size += 1

        def get(self):
            if self.root is None:
                return None
            value = self.root.value
            self.root = self.root.next
            self.size -= 1
            return value

    reverslist = []
    stack = Stack()
    for i in stacklist:
        stack.put(i)
    while not stack.empty():
        reverslist.append(stack.get())
    return reverslist

stacklist = ["1", "2", "3", "4"]
print(is_right_math(stacklist))