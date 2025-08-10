import os

file_name=input("Enter the file name to delete: ")

try:
    if os.path.exists(file_name):
        conformation=input(f"Are you sure to delete {file_name} if (y/n): ").strip().lower()
        if conformation=="y":
            os.remove(file_name)
            print(f"{file_name} is deleted successfully")

        else:
            print("\n file not deleted")

    else:
        raise FileExistsError

except:
    if FileExistsError:
        print("\nFile Not Found")
    if PermissionError:
        print("You dont have permission to access the file!!")