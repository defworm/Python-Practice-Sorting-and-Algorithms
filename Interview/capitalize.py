# Write a recursive function that takes in a list of strings and returns the words capitalized.
# eg: input pandas output PANDAS

def cap_list(in_list):
    #base case
    if len (in_list) == 0:
        return ""
    else:

    #recursive case
        return (f"{in_list[0].upper() } {cap_list(in_list[1:])}")

if __name__ == "__main__":
    list1 = ['karate', 'judo', 'tae kwon do']
    print(cap_list(list1))