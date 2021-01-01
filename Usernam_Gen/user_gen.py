import random
import string
 
 ###################################################
 # APPEND PRINT USERNAME TO .TXT FILE
 ################################################## 
def username_generator():
    
    # get user input
    num = int(input("Number of words to generate: "))
    # read word lists
    with open('./List/nouns.txt', 'r') as infile:
        nouns = infile.read().strip(' \n').split('\n')
    with open('./List/adjec_tives.txt', 'r') as infile:
        adjectives = infile.read().strip(' \n').split('\n')
    #read censor list
    with open('./List/black_list.txt', 'r') as inline:
        censored = inline.read().strip(' \n').split('\n')
    
    # generate usernames
    for i in range(num):

     # construct username
        word1 = random.choice(adjectives)
        word2 = random.choice(nouns)

        #check if word2 is censored
        if word2 in censored:
            i -= 1
            continue
        #else make and print the username
        #captilaize first letter
        word1 = word1.title()
        word2 = word2.title()
        username = '{}{}{}'.format(word1, word2, random.randint(1, 99))
        #print(username)
        print(f"Sucess, Check Text file: \n {username}")

    f = open("./Generated_File/user_name.txt", "a")
    f.write("\n" + username )
    f.close()
        
            
        # success

        
                

        # Write to file


#def save_name():
    
    # print(f"Sucess, Check Text file{username}")
    # f = open("./Usernam_Gen/user_name.txt", "a")
    # f.write(username + "\n")
    # f.close()        

# # open and read the file after the appending:
# f = open("user_name.txt", "r")
# print(f.read())
