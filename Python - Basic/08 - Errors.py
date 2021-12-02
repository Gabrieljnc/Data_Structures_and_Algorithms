# Training Errors

empty_list = []

try:
    empty_list.append(float(input("Type a number --> ")))
    empty_list.append(float(input("Type a number --> ")))
    division = empty_list[0] / empty_list [1]


except ValueError:
    print("You type a string, you have to type a float number")
    
except ZeroDivisionError:
    print("You type 0, Error in the division")
    
except IndexError:
    print("Out of index")
    
except KeyboardInterrupt:
    print("Code interrupted")

else:
    print(f"The result is --> {division}")
    
