import numpy as np 

class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1 
        self.__stack = np.empty(self.__capacity, dtype = int)

    def empty_stack(self):
        if self.__top == -1:
            return True
        else:
            return False
    
    def full_stack(self):
        if self.__top == self.__capacity - 1:
            return True
        else:
            return False

    def pile(self, value_to_pile):
        if self.full_stack():
            print("Stack is full")
        else:
            self.__top += 1
            self.__stack[self.__top] = value_to_pile
    
    def unstack(self):
        if self.empty_stack():
            print("Stack is empty")
        else:
            self.__top -= 1
    
    def see_top(self):
        if self.__top != -1:
            print(self.__stack[self.__top])
            return self.__stack[self.__top]
        else:
            return -1

# Testing Code

stack = Stack(5)

# Pile Function
stack.pile(1)
stack.pile(2)
stack.pile(3)
stack.pile(4)
stack.pile(5)

# See top Function
stack.see_top()

# Unstack Function
stack.unstack()

# See top Function
stack.see_top()