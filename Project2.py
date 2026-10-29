
print("Printing current and previous number sum in a range(10)")
previous_num = 0

for i in range(10):
    current_num = i
    sum_of_numbers = previous_num + current_num
    print(f"Current Number: {current_num}, Previous Number: {previous_num}, Sum: {sum_of_numbers}")
    previous_num = current_num