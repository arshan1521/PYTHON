colors_input = input("Enter comma-separated color names: ")

colors_list = [color.strip() for color in colors_input.split(',')]

print("Colors List:", colors_list)

if colors_list:
    print("First color:", colors_list[0])
    print("Last color:", colors_list[-1])
else:
    print("No colors entered.")
