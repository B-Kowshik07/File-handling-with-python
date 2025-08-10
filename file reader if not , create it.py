import os

file_name=input("\n ENter the file name: \n")
if os.path.exists(file_name):
    print("File exists! printing the contents :")
    with open(file_name,"r") as file:
        print(file.read())

else:
    print("\n file dos'nt exist , creating a new file with default meassage!!")

    with open(file_name,"w") as file:
        file.write("this is an default message!!")

        print(f"file {file_name} created successfully with default meassage")

