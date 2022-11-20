# Another way to reverse a string

def reverse(str):
    string = " "
    for i in str:
        string = i + string
    return string

str = "do not invest in crypto"
print ("The original string is:", str)
print ("The reverse string is:", reverse(str))