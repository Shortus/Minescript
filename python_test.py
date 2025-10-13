test_list = [[1, 5, 3], [1, 2, 3], [2, 5, 8]]
print(test_list)

test_list_str = str(test_list)
print(test_list_str)

list_of_test_list_str = test_list_str.split(",")
print(list_of_test_list_str)

test_output = "\n".join(test_list)
print(test_output)