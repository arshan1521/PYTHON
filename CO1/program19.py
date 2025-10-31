def remove_even_numbers(nums):

    result = [num for num in nums if num % 2 != 0]
    return result

input_numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
output_numbers = remove_even_numbers(input_numbers)
print("List after removing even numbers:", output_numbers)
