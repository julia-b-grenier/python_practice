import math

def sine_of_angle(angle_in_degrees):
    """(float) -> float
    Returns the sine value of angle_in_degrees
    
    
    >>>> sine_of_angle(90)
    1.0
    >>>> sine_of_angle(270)
    -1.0
    >>>> sine_of_angle(360)
    0.0
    """
    angle_in_radians = math.radians(angle_in_degrees)
    sine_value = math.sin(angle_in_radians)
    return round(sine_value,2)

print(sine_of_angle(float(input())))