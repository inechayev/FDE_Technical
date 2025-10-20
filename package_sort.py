def validate_type(value, variable_name):
    """
    validates the type and raises a TypeError if number is not an int or float
    or raises a value error if number is 0 or less since a negative or 0 weight, or dimension
    in three-dimensional space is not valid
    """
    if not isinstance(value, (int, float)):
        raise  TypeError(f'Invalid Type for {variable_name}')
    if value <= 0:
        raise ValueError(f'Invalid Value for {variable_name}')

def sort(width: float, height: float, length: float, mass:float) -> str:
    """
        validates inputs and throws an error on invalid numbers, once validation
        passes, returns string either "STANDARD", "SPECIAL" or "REJECTED" based on
        pre-defined sort logic
    """
    bulky = False
    heavy = False
    validate_type(width, 'width')
    validate_type(height, 'height')
    validate_type(length, 'length')
    validate_type(mass, 'mass')

    #volume in centimeters cubed
    volume = width * height * length

    #check each dimension to determine if it is bulky
    if width >= 150 or height >= 150 or length >= 150 or volume >= 1000000:
        bulky = True

    if mass >= 20:
        heavy = True

    if bulky and heavy:
        return 'REJECTED'
    elif bulky or heavy:
        return 'SPECIAL'
    else:
        return 'STANDARD'

if __name__ == '__main__':
    #values to test with
    width = 1
    height = 1
    length = 1
    mass = 1

    print(sort(width, height, length, mass))


