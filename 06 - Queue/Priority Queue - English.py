'''
Name: Gabriel de Jesus Nunes da Costa
Objective: Create a priority Queue, where the lowest number the more at the beginning of the queue it will be
'''

# Libraries

import numpy as np 
from colorama import Fore

class Queue_Priority():
    def __init__(self, capacity):
        self.capacity = capacity
        self.number_elements = 0
        self.queue = np.empty(self.capacity, dtype = int )

    def empty_queue(self):
        return self.number_elements == 0

    def full_queue(self):
        return self.number_elements == self.capacity

    def all_elements(self):
        if self.empty_queue():
            print(f"\n{Fore.RED}The queue is empty\n")
            return
        else:
            for i in range(6):
                print(i, self.queue[i])
                return

    def enqueue(self, value_to_enqueue):
        if self.full_queue():
            print(f"{Fore.RED} The queue is full\n")
            return

        if self.number_elements == 0:
            self.queue[self.number_elements] = value_to_enqueue
            self.number_elements += 1

        else:

            x = self.number_elements - 1 

            while x >= 0:
                if value_to_enqueue > self.queue[x]:
                    self.queue[x + 1] = self.queue[x]
                else:
                    break
                x -= 1
            
            self.queue[x + 1] = value_to_enqueue
            self.number_elements += 1

    def dequeue(self):
        if self.empty_queue():
            print(f"\n{Fore.RED} The queue is empty\n")
            return

        value_to_dequeue = self.queue[self.number_elements - 1]
        self.number_elements -= 1
        print(f"{Fore.GREEN} {value_to_dequeue} --> was the value dequeue \n")
        return value_to_dequeue

    def first_element(self):
        if self.empty_queue():
            print(f"\n{Fore.RED} The queue is empty\n")
            return -1 

        print(f"{Fore.GREEN} {self.queue[self.number_elements - 1]} --> is the first element\n")
        return self.queue[self.number_elements - 1]



# ------------- Testing the Code ------------- #

queue = Queue_Priority(5)

# ------------- Enqueueu Function ------------- #

queue.enqueue(3)
queue.enqueue(10)
queue.enqueue(4)
queue.enqueue(6)
queue.enqueue(7)

print(f"\n {Fore.WHITE}The queue --> {Fore.CYAN}{queue.queue}\n")

queue.enqueue(13)  # Testing if the queue is full


# ------------- Dequeue Function ------------- #

queue.dequeue() # Dequeue number 3 

# ------------- Enqueue again ------------- #
queue.enqueue(13) 

print(f"\n {Fore.WHITE}The new queue --> {Fore.CYAN}{queue.queue}\n")

# ------------- First element ------------- #

queue.first_element()







