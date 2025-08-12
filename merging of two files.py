file_1=input("Enter the first file name: ")
file_2=input("Enter the second file name: ")

output="merged_file.txt"

try:
    with open(file_1,"r") as f1 ,open(file_2,"r") as f2,open(output,"w") as out:

        out.write(f1.read()+"\n")
        out.write(f2.read())

        print(f"{output} is merged sucessfully!!")

except FileNotFoundError:
    print("File not found!!")