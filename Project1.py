
def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product > 1000:
        return num1 + num2
    else:
        return product

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = multiplication_or_sum(num1, num2)
print("The result is:", result)