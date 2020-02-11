import pandas as pd
import numpy as np

#We first define the function determining the amount of fuel required for each module
def fuel_required(mass_module):
    required_fuel_amount=np.floor(mass_module/3)-2
    return(required_fuel_amount)

#the following shows that the function works with the examples provided
input_example_one=12
input_example_two=14
input_example_three=1969
input_example_four=100756
mass_mehdi=83

print( 'For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get: ', 
      fuel_required(input_example_one))

print( 'For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also', 
      fuel_required(input_example_two))

print( 'For a mass of 1969, the fuel required is: ', 
      fuel_required(input_example_three))

print( 'For a mass of 100756, the fuel required is: ', 
      fuel_required(input_example_four))

print( 'For a mass of ',mass_mehdi, ', the fuel required is: ', 
      fuel_required(mass_mehdi))

#Sum of all of these

mass_modules = np.matrix([112908,  61769,  65967,  51494,  99689, 114098, 135346,  59561,
         147324,  50465, 117491,  77845,  91959,  59847,  84013,  85763,
          62121,  58965,  89809,  97870,  77696,  70218, 118404,  83505,
         141729,  61534, 101073, 131358,  76104, 120836, 109789,  96510,
          65406, 117906,  74921,  95412,  99875, 134298, 105235,  82802,
         103392,  81906, 133786, 140681, 109004, 148434,  92333,  83848,
          98297,  95728, 138202,  79312,  55633, 138461,  50293, 141922,
         140303,  66542,  50054,  99076, 143201,  66702, 133583,  70308,
         146824,  95606,  63054, 129272, 133051,  58626, 119896,  66265,
          99925, 131752,  74669, 148387, 132124, 107188,  55535, 145004,
          78122,  50885,  70325, 100859,  86484,  88795, 148164,  64473,
         143089, 121023,  52904, 120927,  87164, 133709,  89427, 105350,
         106378,  98492,  78394, 145200])

total_fuel_required=fuel_required(mass_modules).sum()
print('The total fuel requirements for the modules in the aircraft is:',
      total_fuel_required)
