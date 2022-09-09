_FLAG = "Y"

while _FLAG == "Y":
  number = int(input("Type a number and i'll check if it is even or odd: "))

  if (number % 2 == 0):
    print(f"The number {number} is even.")
  else:
    print(f"The number {number} is odd.")

  _FLAG = str(input("Wanna check another number? [Y]/[N]: ")).upper()
  