def add(num1, num2):
    if not (isinstance(num1, int) and isinstance(num2, int) or \
        isinstance(num1, float) and isinstance(num2, float) or \
        isinstance(num1, str) and isinstance(num2, str)):
        raise ValueError(f"Incompatible types of parameter: {type(num1)} and {type(num2)}")       
    return num1 + num2

def divide(num1, num2):
    if not (isinstance(num1, int) and isinstance(num2, int) or \
        isinstance(num1, float) and isinstance(num2, float)):
        raise ValueError(f"Incompatible types of parameter: {type(num1)} and {type(num2)}")
    if num2 == 0:
        raise ArithmeticError("Can not divede by zero!!!")
    return num1 / num2