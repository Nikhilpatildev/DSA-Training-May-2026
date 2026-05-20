#function
def hello():
    print("Hello World")

hello()

def arithmetic():
    a = int (input("Enter first number: "))
    b = int (input("Enter second number: "))
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div
result = arithmetic()
print("Sum: ", result[0])
print("Sub: ", result[1])
print("Mul: ", result[2])
print("Div: ", result[3])

#how many types of arguments we pass in function
# 1. Positional arguments
# 2. Keyword arguments
# 3. Default arguments
# 4. Variable length arguments

#keyword arguments
def crdentials(username, password):
  if username == password:
    print("login successful")
  else:
    print("login failed")
crdentials(username = "admin", password = "admin")   

