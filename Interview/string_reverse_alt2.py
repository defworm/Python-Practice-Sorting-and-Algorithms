# Another version of string reversal

def reverse_string(test_string):
    if len(test_string) == 0 or len(test_string) == 1:
        return test_string
    else:
        return test_string[len(test_string) -1] + reverse_string(test_string[:len(test_string)-1])

test_string= "you are only young once"

print(reverse_string(test_string))