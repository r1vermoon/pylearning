#函数
def greet_user(username):
    print("Hello, "+username.title()+"!")

greet_user("jesse")

#返回值
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()
musician=get_formatted_name('jy','J')
print(musician)

#列表
def greet_users(names):
    for name in names:
        print(name.title())

usernames=['jjy','mxy']
greet_users(usernames)

#空元组
def make_pizza(*toppings):
    print(toppings)

make_pizza('apple')
make_pizza('mushroom')

#字典封装
def build_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value

    return profile

user_profile=build_profile('albert','einstein',
                           location='princeton',
                           field='phtsics')
print(user_profile)

