# Import library

import numpy as np

# Creating Class

class Ordered_Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.array = np.empty(capacity, dtype = int)

    
    # Print Function

    def Print(self):
        if self.last_position == -1:
            print("Empty Array")
        else:
            for i in range(self.last_position + 1):
                print(i, "-->", self.array[i])
            
    # Insert Function

    def Insert(self, value_to_insert):

        if self.last_position == self.capacity - 1:
            print("Array is full")

        else:
            position = 0

            for i in range(self.last_position + 1):
                position = i 
                
                if self.array[i] > value_to_insert:
                    break
                
                if i == self.last_position:
                    position = i + 1

            last_position = self.last_position
            
            while last_position >= position:
                self.array[last_position + 1] = self.array[last_position]
                last_position -= 1

            self.array[position] = value_to_insert
            self.last_position += 1 

    # Linear Search Function

    def Linear_Search(self, value_to_search):
        
        for i in range(self.last_position + 1):
            if self.array[i] == value_to_search:
                print(f"\nValue found in {i} position")
                return i 

            elif self.array[i] > value_to_search:
                print("V\nValue not Found")
                return -1
            
            elif i == self.last_position:
                print("\nValue not Found")
                return -1 
            
    # Binary Search Function

    def Binary_Search(self, value_to_search):
        lesser_limit = 0
        upper_limit = self.last_position

        while True:

            mid_position = int((lesser_limit + upper_limit) / 2)

            if self.array[mid_position] == value_to_search:
                print(f"\nValue found in {mid_position} position")
                return mid_position
            
            elif lesser_limit > upper_limit:
                print("\nValue not Found")
                return -1 
            
            else:
                if self.array[mid_position] < value_to_search: # Value is in the right side of the array or doesnt exist
                    lesser_limit = mid_position + 1

                else:
                    upper_limit = mid_position - 1 # Value is in the left side of the array or doesnt exist
            
    # Remove Function

    def Remove(self, value_to_remove):
        position = self.Binary_Search(value_to_remove)

        if position == -1:
            print("\nValue not found to remove")
            return -1
        
        else: 
            for i in range(position, self.last_position):
                self.array[i] = self.array[i + 1]
        
        self.last_position -= 1

# Testing
array = Ordered_Array(5)

array.Insert(5)
array.Insert(65)
array.Insert(35)
array.Insert(25)
array.Insert(15)

array.Linear_Search(25)
array.Binary_Search(15)

array.Remove(25)

array.Print()

            


    
