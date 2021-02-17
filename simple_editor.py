# Program 1 Simple Editor
# version python 3.8
# read, write, delete, rename
import os
print("This is a command line text editor. You can read, write, delete and rename a file.")
file_name = input("Please enter the file that you want to edit: (make sure that your name contains the .txt)")


def read():
    text_file = open(file_name, 'r')
    # get the list of line
    line_list = text_file.readlines()
    # for each line from the list, print the line
    for line in line_list:
        print(line)
    text_file.close()


def write():
    text_file = open(file_name, 'a')
    write_data = input("Please enter data: ")
    text_file.write(write_data)
    text_file = open(file_name, 'r')
    print("You have successfully changed the content! The edited file is: ")
    print(text_file.read())


def delete():
    os.remove(file_name)


def rename():
    new_name = input("Enter the new file name: (make sure that your name contains the .txt)")
    global file_name
    os.rename(file_name, new_name)
    file_name = new_name
    print("Your file has been successfully renamed! The current file name is:")
    print(file_name)


keepAlive = True
while keepAlive:
    user_input1 = input("Please enter your command: ")
    if user_input1 == "read":
        read()
    elif user_input1 == "write":
        write()
    elif user_input1 == "delete":
        delete()
    elif user_input1 == "rename":
        rename()
    elif user_input1 != ("read" and "write" and "delete" and "rename"):
        print("Sorry, the command can only be read, write, delete and rename.")
    user_input2 = input("Do you want to edit the file again?: (Y/N)")
    if user_input2 == "N":
        keepAlive = False
    elif user_input2 == "Y":
        keepAlive = True
    else:
        print("Sorry, the command can only be Y or N.")
        user_input2 = input("Do you want to edit the file again?: (Y/N)")




