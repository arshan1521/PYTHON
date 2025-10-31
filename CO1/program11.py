file_name = input("Enter the file name: ")

dot_position = file_name.rfind('.')

if dot_position != -1 and dot_position != len(file_name) - 1:
    
    extension = file_name[dot_position + 1:]
    print("Extension of the file is:", extension)
else:
    print("No extension found in the file name.")
