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
mass_modules=np.matrix([input_example_one,input_example_two,input_example_three,input_example_four,mass_mehdi])
total_fuel_required=fuel_required(mass_modules).sum()
print('The total fuel requirements for the modules in the aircraft are:',
      total_fuel_required)
