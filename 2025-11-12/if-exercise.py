# if-else-elif exercise

input:int = input("Insert a number between 1 and 3: ")
if input == 1: print("you chose 1")
elif input == 2: print("you chose 2")
elif input == 3: print("you chose 3")
else: print("I said between 1 and 3")
quit()


usernames = ['pippo_baudo_32','Fantasy_killer_xx','FedericoPinna9']
while True:
    user_name:str = input("insert username: ")

    if not user_name in usernames:
        usernames.append(user_name)
        user_pw:str = input("Insert password: ")
        user_id:int = len(usernames)
        break
    else:
        print("username already exists, try again")



