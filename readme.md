# FDE Technical

## Project Overview
Sort Function implementation per the instructions, 
may be nice to eventually make this a class method but 
the implementation was done exactly to the assignment spec


## sort()
Takes width (cm), height (cm), length (cm)  and mass (kg) parameters. 


If volume (width\*height\*length) is greater than or equal to 1000000 centimeters
cubed package is bulky

If mass > 20 KG package is heavy.

Function returns a string:
- STANDARD: Package is neither heavy nor bulky
- SPECIAL: Package is heavy or bulky
- REJECTED: Package is both heavy and bulky

String is currently printed to the console. Another option would be to build a dict
if a unique identifier exists for each package, that has the key as the identifier and the 
sorting as the value. 

### Validation:
sort() will raise an error if an invalid value is provided and stop operation
another option is to log the error and automatically return REJECTED but I went 
with the complete stop route