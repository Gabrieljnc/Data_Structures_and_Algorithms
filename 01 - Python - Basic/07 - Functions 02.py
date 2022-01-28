# Code to calculate the quantity of liters used in one travel

def read_data():
    km_liters = float(input("\nEnter how many liters the car do in one Kilometer --> "))
    time_travel = float(input("Enter the time spent in the travel --> "))
    average_speed = float(input("Enter the average speed in the travel --> "))

    return km_liters, time_travel, average_speed


def distance_calculator(time_travel,average_speed ):
    travelled_distance = time_travel * average_speed
    return travelled_distance

def used_liters(travelled_distance, km_liters):
    used_liters = round((travelled_distance / km_liters),2)
    return used_liters

def show_values(average_speed, time_travel, travelled_distance, used_liters):
    print(f"\nThe average speed is --> {average_speed}")
    print(f"The time spent in the travel is --> {time_travel}")
    print(f"The travelled distance is --> {travelled_distance}")
    print(f"The total of used liters is --> {used_liters}")


# Applying the code

km_liters, time_travel, average_speed = read_data()

# The distance of the travel
travelled_distance = distance_calculator(time_travel, average_speed)

# Used liters in the travel
used_liters = used_liters(travelled_distance, km_liters)

# Show the values
show_values(average_speed, time_travel, travelled_distance, used_liters)
