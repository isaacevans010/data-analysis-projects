# 1. Declare and assign the variables here:
name = "f-string"
name_of_space_shuttle = "Determination"
shuttle_speed = 17500
distance_to_mars = 225000000
distance_to_moon = 384400
miles_per_km = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(name)
print(name_of_space_shuttle)
print(shuttle_speed)
print(distance_to_mars)
print(distance_to_moon)
print(miles_per_km)

# Code your solution to exercises 3 and 4 here:
# ex. 3 answers
miles_to_mars = (distance_to_mars) * (miles_per_km)
hours_to_mars = (miles_to_mars)/(shuttle_speed)
days_to_mars = hours_to_mars/24
#ex. 4 answers
print({name_of_space_shuttle},"will take", {days_to_mars}, "days to reach Mars.")


# Code your solution to exercise 5 here
miles_to_moon = (distance_to_moon) * (miles_per_km)
hours_to_moon = (miles_to_moon)/(shuttle_speed)
days_to_moon = hours_to_moon/24
print({name_of_space_shuttle},"will take", {days_to_moon}, "days to reach the moon.")
