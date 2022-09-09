def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return False
  return x / y

assert add(1, 2) == 3, "The sum of 1 and 2 should be 3."

assert subtract(30, 15) == 15, "The subtraction of 30 and 15 should be 15."

assert subtract(10, 15) == -5, "The subtraction of 10 and 15 should be -5."

assert multiply(5, 3) == 15, "The multiplication of 5 and 3 should be 15."

assert divide(8, 2) == 4, "The division of 8 and 2 should be 4."

assert divide(10, 0) == False, "The division of 10 and 0 should be impossible and return False."