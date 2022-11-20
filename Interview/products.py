# Write a funtion that takes in a list of numbers and returns the product of the numbers in the list
# eg: input 4, 3, 5 output 60

def multiply_list(in_list):
    total = 1
    if len(in_list) == 0:
        return 0

    elif len(in_list) == 1:
        return in_list[0]
    else:
        for num in in_list:
            total *= num
        return total

if __name__ == "__main__":
    list1= [4, 3, 5, 9]
    print(multiply_list(list1))