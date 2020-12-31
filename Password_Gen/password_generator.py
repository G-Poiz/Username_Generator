import random
import os.path

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^' , '*', ':' , ';' ,'"', "'", '?', '<', '>', '/', '.', ',','{','}', '[', ']','|','+', '-', '*', '=', '_', '~', '`' ]



def password_generator():
    question1 = input("Which type of Password would you like to Generate? (Random or Option2)\n").lower()

    if  question1 == 'random':
        rand_password()
    elif question1 == 'option2':
        insert_own_password()
    else:
        print("Error!!")

def insert_own_password ():
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Set Password in  list []
    password_list = []
    for char in range(1, nr_letters + 1):
        password_list += random.choice(letters)
    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)
    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    #print(password_list)

    # Shuffle the Password_list '
    password = " "
    random.shuffle(password_list)
    for char in password_list:
        password += char 
    #print(f"Password:{password}")

    #When done save file to folder
    save_path_function()

#password_list = []
#password = " "    
def rand_password():
    total_list = (letters + numbers + symbols)
    #print(total_list)
    #nr_password = int(input(f"Number of Passwords:\n"))
    nr_characters = int(input(f"Length of Password(s):\n"))

    password_list = []
    for pwd in range(nr_characters):
        password_list += random.choice(total_list)
    #print(password_list)

    #     Shuffle
    password =" "
    random.shuffle(password_list)
    for chars in password_list:
        password += chars
    #print(f"Password:{password}\n")
    f = open("Password_Gen.txt", "a" )
    f.write( password +"\n" )
    f.close()
    #When done save file to folder
    #save_path_function()
rand_password()

#password = " "

def save_path_function():
    file_name =input("Do you want it to save in the last place as before? (Y/N)\n('Password_Gen1')\n").lower()
    if file_name == "y":
        save_Path = "C: \\Users\\ok\\Documents\\Codes\\Projects\\MyProjects\\Username_Generator\\Generated_File"

        f = open("Password_Gen.txt", "a" )
        f.write( password +"\n" )
        f.close()

    else:
        save_Path = "C: \\Users\\ok\\Documents\\Codes\\Projects\\MyProjects\\Username_Generator\\Generated_File\\"
        name = input ( "File Name:")
        complete_Name = name + ".txt"
        complete_Name = os.path.join(save_Path , name + ".txt")
        f = open( complete_Name , "w")
        #toFile = input("Write what you want into the field")
        #f.write(toFile)
        f.close()        

