
file_1=input("Enter the file name: ")

try:
    with open(file_1,"r") as file:
        lines=file.readlines()

    numbered_lines = [f"{i+1}-{line}" for i, line in enumerate(lines)]

    with open(file_1, "w") as file:

        file.writelines(numbered_lines)

    print("Line numbers added successfully!")

except FileNotFoundError:

    print("Error: File not found. Please check the file name.")
