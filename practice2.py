# Write a Python program to get the smallest number from a list.


def get_smallest_number(input_list):
    if not input_list: 
        return None
    else:
        return min([x for x in input_list])

my_list = [3, 1, 4, 2, 5]

smallest_number = get_smallest_number(my_list)

print("The smallest number in the list is:", smallest_number)