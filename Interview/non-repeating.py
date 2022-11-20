# Write an algorithm that prints the non-repeating integers in a list
# eg: input 1, 5, 1, 5, 6, 8 output 6, 8

def no_repeat(in_list):
    #Count the number of times an item appears
    items={}
    for i in range(len(in_list)):
        if in_list[i] not in items:
            items[in_list[i]] = 1
        else:
            items[in_list[i]] += 1
    print(items) #bonus: this will keep a dictionary w/ number of each character.
        
    for key in items:
        if items[key] == 1:
            print(key)

if __name__ == "__main__":
    list1 = [1, 5, 1, 5, 8, 6]
    list2 = "this is a list of characters"
    no_repeat(list2)