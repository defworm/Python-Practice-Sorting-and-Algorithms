# Write a function that takes in a string and returns the string reversed
# eg: input "hello", out put "olleh"

def reverser(in_string):
    return in_string[::-1] #::1 reverses a string in python
if __name__ == "__main__":
    string1 = "Did Hannah see bees? Hannah did."
    print(reverser(string1))