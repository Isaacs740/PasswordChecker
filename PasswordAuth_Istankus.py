import re

# dict for ID/PW
user = {}


try:
    f = open('dictionary.txt', 'r')
    for key in user.items():
        f.readlines(key)
        if not user.items():
            break
except FileNotFoundError:
    print('Cannot find dictionary file...using default dictionary')
    user = {'george7': 'Myid79',
            'maryb2': 'Watchh809'}


# Checks for letters, numbers, and length of input
def checker(x):
    if not re.search("[a-zA-Z]", x):
        print('Response does not contain at least one letter.')
        return False
    elif not re.search("[0-9]", x):
        print('Response does not contain at least one number.')
        return False
    elif len(x) < 6:
        print('Response is too short. Minimum 6 characters required. ')
        return False
    else:
        return True


validate = False
while not validate:
    username = input('Please enter userid \n')
    validate = checker(username)
    continue

v = False
while not v:
    password = input("Please enter password (case sensitive)\n")
    v = checker(password)
    continue

# loop looking for users in dict
while True:
    if username in user:
        if user[username] == password:
            break
    elif username != user:
        add = input('User not found. Do you wish to add this? (Y/N)\n')
        if add == 'y':
            print('User ' + username + ' added.\n')
            user[username] = password
            print('Request complete. \nWriting the Dictionary......')
            print('\t......Dictionary update complete\n Thank you for using Password Check.')
            f = open('dictionary.txt', 'a')
            for key, value in user.items():
                f.write(key + ':' + value + '\n')
            f.close()
        else:
            if add == 'n':
                print('User ' + username + ' not added.')
                break
