from Password_Gen.password_generator import password_generator
from Usernam_Gen.user_gen import username_generator




print("Welcome to G-Generator:")
question_1 = input("What would you like to generate today?(Username or Password)\n").lower()

if question_1 == 'password':
    password_generator()
elif question_1 == 'username':
    username_generator()
