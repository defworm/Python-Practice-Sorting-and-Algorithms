
# def value(r):
#     if (r == "I"):
#         return 1
#     if (r == "V"):
#         return 5
#     if (r == "X"):
#         return 10
#     if (r == "L"):
#         return 50
#     if (r == "C"):
#         return 100
#     if (r == "D"):
#         return 500
#     if (r == "M"):
#         return 1000
#     return -1

# def romanToInt(str):
#     res = 0
#     i = 0

#     while (i < len(str)):
#         s1 = value(str[i])

#         if (i + 1 < len(str)):
#             s2 = value(str[i + 1])

#             if (s1 >= s2):
#                 res = res + s1
#                 i = i + 1
#             else:
#                 res = res + s2 - s1
#                 i = i + 2
#         else:
#             res = res + s1
#             i + i + 1
#     return res

# input = "M"

# print(f"Integer form of Roman Numeral is {value(input)}")

def romanToInt(s):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        print(f"The interger version of your roman numeral is {number}")
         
romanToInt('MCMI')
