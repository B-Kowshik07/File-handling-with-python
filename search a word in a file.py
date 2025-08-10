import os
from re import search

file_name=input("ENter the file name: \n")

search_word=input("Enter the word to search: \n")

try:
    with open("file_name","r") as file:
        found=False

    for line_number,line in  enumerate(file,start=1):
        if search_word in line:
            print(f"found {search_word} on {line_number}")

            found=True
    if not found:
        print(f"{search_word} is not found\n")

except FileNotFoundError:
    print(f"{file_name} is not found,please try again.")
