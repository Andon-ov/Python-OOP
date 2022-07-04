class Stack:
    def __init__(self):
        self.data: list[str] = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if len(self.data) > 0 else True

    def __str__(self):
        result = self.data[::-1]
        return f"[{', '.join([str(x) for x in self.data[::-1]])}]"

# from typing import List

#
# class Stack:
#     def __init__(self):
#         self.data: list[str] = []
#
#     def push(self, element: str):
#         self.data.append(element)
#
#     def pop(self):
#         return self.data.pop()
#
#     def top(self):
#         return self.data[-1]
#
#     def is_empty(self):
#         return not any(self.data)
#
#     def __str__(self):
#         return "[" + ", ".join(reversed(self.data)) + "]"


# class Stack:
#     def __init__(self):
#         self.data = []
#
#     def push(self, element):
#         self.data.append(element)
#
#     def pop(self):
#         return self.data.pop()
#
#     def top(self):
#         return self.data[-1]
#
#     def is_empty(self):
#         if not self.data:
#             return True
#         return False
#
#     def __str__(self):
#         return f"[{', '.join([x for x in self.data])}]"
