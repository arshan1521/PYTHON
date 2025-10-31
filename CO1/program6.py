def check_lists(list1, list2):
    same_length = len(list1) == len(list2)
    same_sum = sum(list1) == sum(list2)
    common_values = set(list1).intersection(set(list2))
    any_common = len(common_values) > 0
    return same_length, same_sum, any_common, common_values

list1 = list(map(int, input("Enter integers for list 1 separated by spaces: ").split()))
list2 = list(map(int, input("Enter integers for list 2 separated by spaces: ").split()))

results = check_lists(list1, list2)
print(f"Same Length: {results[0]}")
print(f"Same Sum: {results[1]}")
print(f"Any Common Values: {results[2]}")
print(f"Common Values: {results[3]}")
