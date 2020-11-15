def get_answer(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('yes',  'y',  'accept' ):
            return "You have Accepted!"
            
        elif  answer in ('no',  'n','decline'):
           return "You have Declined!"
            
print(get_answer("This content includes sencitive content 'Accept' or 'Decline'?"))
