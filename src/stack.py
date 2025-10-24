class Stack:
    lst = []

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        if not self.lst:
            raise IndexError("pop from empty stack")
        return self.lst.pop()

    def peek(self):
        if not self.lst:
            raise IndexError("peek from empty stack")
        return self.lst[-1]

    def is_empty(self) -> bool:
        return not self.lst

    def __len__(self) -> int:
        return len(self.lst)
