##############################################################################
#  Computer Project #1
#  
#  Algorithm
#     Establishment of constants 
#     Prompt for race and tortoise speed
#     Calculation of the time the tortoise takes
#         Display of the time the tortoise takes to complete the race
#     Prompt for hare speed, hare rest time, and length of time the hare runs
#     Multi-step calculation of the time the hare takes to complete the race
#         Display of the time the hare takes to complete the race
##############################################################################

#Constants
miles_conv = 0.0095 #Conversion factor of inches/minute to miles/hour
hours_conv = 60 #Conversion of minutes to hours

#Input for the race length
num_str = input( "What is the Length of the race, in miles? " ) 
num_float = float( num_str ) 
race = num_float #Race length

#Input for the tortoise speed
num_str = input( "What is speed of the tortoise, in inches per minute? " ) 
num_float = float( num_str ) 
tortoise = num_float * miles_conv #Tortoise speed 

#Display of the tortoise time for the race
tortoise_time = ( race / tortoise )
print("The tortoise finishes the race in", tortoise_time, "hours." )

#Input for the hare speed
num_str = input( "What is speed of the hare, in miles per hour? " ) 
num_float = float( num_str ) 
hare_speed = num_float #Hare speed

#Input for the hare resting time
num_str = input( "How many minutes does the hare rest at a time? " ) 
num_float = float( num_str ) 
hare_rest = num_float / hours_conv #Hare resting time

#Input for the minutes the hare runs at a time 
num_str = input( "How many minutes does the hare run at a time? " ) 
num_float = float( num_str ) 
hare_endurance = num_float / hours_conv #Length of time the hare runs at a time

#Calculation for the distance traveled in one go
hare_performance = hare_speed * hare_endurance #Distance traveled per run

#Calculation for the number of times ran
import math
times_ran = math.ceil( race / hare_performance ) #Amount of times ran

#Calculation for the total time spent running
running_time = race / hare_performance #Total time spent running

#Calculation for the total time spent resting
rest_time = ( times_ran - 1 ) * hare_rest #Total time spent resting

#Display of hare time for the race
total_time = running_time + rest_time
print( "The hare finishes the race in", total_time, "hours." )