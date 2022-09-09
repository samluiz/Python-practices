def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

FLAG = "Y"

while FLAG == "Y":
  print("---------------------------- Welcome to the calculator! ----------------------------\n")
  option = int(input("What do you wanna do? [1] Sum [2] Subtract [3] Multiply [4] Divide: \n"))
  n1 = int(input("Enter the first number: \n"))
  n2 = int(input("Enter the second number: \n"))

  if option == 1: print(f"The sum of {n1} and {n2} is {add(n1, n2)}.")
  if option == 2: print(f"The subtraction of {n1} and {n2} is {subtract(n1, n2)}.")
  if option == 3: print(f"The multiplication of {n1} and {n2} is {multiply(n1, n2)}.")
  if option == 4 and n2 != 0:
    print(f"The division of {n1} and {n2} is {divide(n1, n2)}.")
  else:
    print("You can't divide by zero.")

  FLAG = str(input("Wanna calculate more? [Y]/[N]: ")).upper()