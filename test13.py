import json

username=input("Your name:")

filename='username.json'
with open(filename,'w') as file:
    json.dump(username,file)
    print("We will remember "+username+"!")

with open(filename) as file1:
    username=json.load(file1)
    print("Welcome back "+username+".")

def get_stored_username():
    filename='username.json'
    try:
        with open(filename) as filepro1:
            username=json.load(filepro1)
    except FileNotFoundError:
        return None #pass
    else:
        # username=input("Your name:")
        return username
    
def get_new_name():
    username=input("Your name:")
    filename='username.json'
    with open(filename,'w') as filepro:
        json.dump(username,filename)
    return username

def greet_user():
    username=get_stored_username()
    if username:
        print("Hello "+username+'.')
    else:
        username=get_new_name()
        print("We will remember "+username+'.')

greet_user()