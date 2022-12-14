# Write a recursive function that takes in a nmumber and returns the sum of the numbers from 0 to the number.
# Eg. If the input is 5, the expected output would be 15 (5+4+3+2+1= 15)

def sum_of_all_numbers(num):
    # base case
    if num == 0 or num == 1:
        return num
    else: 
        # recursive case
        return num + sum_of_all_numbers(num-1)

n=6

print(f"The sum of all numbers in {n} is {sum_of_all_numbers(n)}")