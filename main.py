from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))

for symbols in operations:
  print(symbols)
operation_symbol = input("Pick an operation from the line above: ")

