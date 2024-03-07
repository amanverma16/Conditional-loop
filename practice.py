def get_unique_elements(input_list):
    unique_set = set(input_list)
    unique_list = list(unique_set)
    
    return unique_list

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
result = get_unique_elements(sample_list)
print("Sample List:", sample_list)
print("Unique List:", result)
