import random
import string

# hardcoding a bunch of usernames
usernames = [
    "pippo_baudo_32",
    "Fantasy_killer_xx",
    "FedericoPinna9",
    "cool_cat_77",
    "skywalker_2025",
    "dragonSlayerX",
    "coffee_addict_01",
    "mountain_hiker88",
    "tech_guru_42",
    "bookworm_luca"
]

# defining a function that takes random characters and joins em together
def random_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation # creates array full of characters
    return ''.join(random.choice(chars) for _ in range(length)) # selects some random chars for password by given length

# creating passwords
passwords = [random_password() for _ in range(len(usernames))]

# ---
# Remove '#' before *print(passwords)* to have a look at the randomly generated passwords
# ---
#print(passwords)



# arbitrary variable asked on point 4
ISLOGGED = False

if ISLOGGED == True:
    # asking security questions if point 4 is active
    quastion:str=input("What's your first pet's name?")
        # Answer hard coded as for exercise request. Sets a boolean, if true proceeds
    match quastion:
        case "snuffles": question_bool = True 
        case _: question_bool = False
    if question_bool:
        quastion=input("What's your mother's name?")
        # Answer hard coded as for exercise request. Sets a boolean, if true proceeds
        match quastion:
            case "Janet": question_bool = True 
            case _: question_bool = False
    if question_bool:
        #if both questions are correct, greets the default user
        print("Welcome, cool_cat_77!")
else:
    # asks user for username and password as for exercise description
    user_name = input("Insert username: ")
    user_pw = input("Insert password: ")
    if user_name in usernames:
        #checks if username and pw are correct, then logs in (This is for logical-purpose only, it's not meant to be secure)
        if user_pw == passwords[usernames.index(user_name)]:
            print(f"Welcome {user_name}!!")
        else:
            print("Wrong password!")
    else:
        # registers user if not present
        usernames.append(user_name)
        passwords.append(user_pw)
        print("User registered succsesfully!")