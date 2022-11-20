#1. Write an algorithm that checks if a string contains another string

# If it does, return True; otherwise, return False

# Eg: When checking if string “Hello world” contains “Hello”, the function should return True. If checking the same string contains “Bye”, the function should return False.


def string_check(in_string, find_str):
	if find_str in in_string:
		return True
	else:
		return False

if __name__ =="__main__":
	string1 = "This is a string that has some words in it"
	string2 = "has some words"

print(string_check(string1, string2))
