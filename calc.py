# calc.py
from math import sqrt
def calculate(current_value, num, clear):
    if clear:
        return ''  # Clear the current value if clear button is pressed
    elif num:
        if num == '=':
            # Calculate result if '=' is pressed
            try:

                # Safely evaluate the current expression
                return str(eval(current_value))
            except:
                return 'Error'
        else:
            if num == "^":
                return float(current_value)*float(current_value)
            if num == "sqrt":
                return sqrt(float(current_value))
            # Append the pressed button value to the current value
            return current_value + num
    return current_value
