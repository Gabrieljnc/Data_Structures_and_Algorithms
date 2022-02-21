import numpy as np 

class Circular_Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.start = 0
        self.end = -1 
        self.number_elements = 0
        self.queue = np.empty(self.capacity, dtype = int)
            

    def queue_empty(self):
        return self.number_elements == 0
    
    def queue_full(self):
        return self.number_elements == self.capacity

    def all_elements(self):
        if self.queue_empty():
            print("The queue is empty")
            return -1 
        else:
            for i in range(self.capacity):
                print(i, "-->", self.queue[i])


    def rank(self, value_to_rank):
        if self.queue_full():
            print("The Queue is Full")
            return 
        
        if self.end == self.capacity - 1:
            self.end = -1 
        
        self.end += 1
        self.queue[self.end] = value_to_rank
        self.number_elements += 1

    def dequeue(self):
        if self.queue_empty():
            print("The queue is empty")
            return 
        
        queue_first_element = self.queue[self.start]
        self.start += 1

        if self.start == self.capacity - 1:
            self.start = 0 
        
        self.number_elements -= 1
        return queue_first_element 
    
    def first_element(self):
        if self.queue_empty():
            print("The queue is empty")
            return -1 
        
        print(self.queue[self.start])
        return self.queue[self.start]

# ------------ Testing the code -------------------


# Defining the queue with capacity of 5 numbers 
queue = Circular_Queue(5)

# Ranking 5 elements to the queue 
queue.rank(10)
queue.rank(20)
queue.rank(30)
queue.rank(40)
queue.rank(50)

# Seeing the fisrt element in the queue = 10

queue.first_element()

# Dequeue the first element of the queue

queue.dequeue() 

# Seeing the new fisrt element in the queue = 20
queue.first_element()

# Adding the number 60 in the queue
queue.rank(60)

# Trying add a number bigger than the capacity
queue.rank(70)
