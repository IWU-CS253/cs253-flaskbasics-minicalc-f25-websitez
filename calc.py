# calc.py

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
            # Append the pressed button value to the current value
            return current_value + num
    return current_value


''' Do one at a time
def mod(x,y):
    if y == 0:
        return f"Error: Modulus by zero"
    return x % y

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y
'''
