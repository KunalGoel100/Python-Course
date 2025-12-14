def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2

print("Enter 2 numbers and *, /, +, -")
n1 = int(input())
n2 = int(input())
sign = input()
result = 0
if sign == "*":
    result = multiply(n1, n2)
elif sign == "/":
    result = divide(n1, n2)
elif sign == "+":
    result = add(n1, n2)
elif sign == "-":
    result = subtract(n1, n2)

print(f"Result = {result}")
choice = "y"
while choice == "y":
    choice = input("Want to do more: y, n").lower()
    if choice == "y":
        print("Enter a numbers and *, /, +, -")
        n2 = int(input())
        sign = input()
        if sign == "*":
            result = multiply(result, n2)
        elif sign == "/":
            result = divide(result, n2)
        elif sign == "+":
            result = add(result, n2)
        elif sign == "-":
            result = subtract(result, n2)
        print(f"Result = {result}")


