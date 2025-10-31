color_list1_input = input("Enter colors for list 1, separated by commas: ")
color_list1 = [color.strip() for color in color_list1_input.split(',')]

color_list2_input = input("Enter colors for list 2, separated by commas: ")
color_list2 = [color.strip() for color in color_list2_input.split(',')]

unique_colors = [color for color in color_list1 if color not in color_list2]

print(unique_colors)
