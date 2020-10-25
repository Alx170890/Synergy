brackets = {
    '(':')',
    '{':'}',
}


def is_right_math(equation):
    stack = list()
    for i in equation:
        if i in brackets:
            stack.append(i)
        if i in brackets.values():
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if brackets[last_open] != i:
                return False
    return len(stack) == 0


print(is_right_math('(2+1(2+2)-{2+1})'))


# class EmptyStackException(Exception):
#     pass
#
#
# class Stack:
#     class Node:
#         def __init__(self, value, nextNode):
#             self.value = value
#             self.nextNode = nextNode
#
#     def __init__(self):
#         self.top = None
#
#     def isEmpty(self):
#         return self.top is None
#
#     def push(self, value):
#         self.top = Stack.Node(value, self.top)
#
#     def pop(self):
#         if self.isEmpty():
#             raise EmptyStackException
#         val = self.top.value
#         self.top = self.top.nextNode
#         return val
#
#
# if __name__ == "__main__":
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#
#     while not s.isEmpty():
#         print(s.pop())



# def contains (self, cat):
    #     lastbox = self.head
    #     while (lastbox):
    #         if cat == lastbox.cat:
    #             return True
    #         else:
    #             lastbox = lastbox.nextcat
    #     return False

# def get(self, catIndex):
    #     lastbox = self.head
    #     boxIndex = 0
    #     while boxIndex <= catIndex:
    #         if boxIndex == catIndex:
    #             return lastbox.cat
    #         boxIndex = boxIndex + 1
    #         lastbox = lastbox.nextcat

# def LLprint(self):
    #     currentCat = self.head
    #     print("LINKED LIST")
    #     print("-----")
    #     i = 0
    #     while currentCat is not None:
    #         print (str(i) + ": " + str(currentCat.cat))
    #         i += 1
    #         currentCat = currentCat.nextcat
    #     print("-----")


# class Box:
#     def __init__(self, cat = None):
#         self.cat = cat
#         self.nextcat = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#
#
#     def addToEnd(self, newcat):
#         newbox = Box(newcat)
#         if self.head is None:
#             self.head = newbox
#             return
#         lastbox = self.head
#         while (lastbox.nextcat):
#             lastbox = lastbox.nextcat
#         lastbox.nextcat = newbox
#
#
#
#     def removeBox(self, rmcat):
#         headcat = self.head
#         if headcat is not None:
#             if headcat.cat == rmcat:
#                 self.head = headcat.nextcat
#                 headcat = None
#                 return
#         while headcat is not None:
#             if headcat.cat == rmcat:
#                 break
#             lastcat = headcat
#             headcat = headcat.nextcat
#         if headcat == None:
#             return
#         lastcat.nextcat = headcat.nextcat
#         headcat = None