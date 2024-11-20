#if
cars=['audi','bnw','subaru','toyota']
for car in cars:
    if car=='bnw':
        print(car.upper())
    else:
        print(car.title())

answer=17
if answer!=42:
    print("That is not the correct answer. Please try again!")

banned_users=['andrew','carolina','david']
user='marie'

if user not in banned_users:
    print(user.title()+",you can post a response if you wish.")
print("------------------")

game_active=True
can_edit=False

age=67
if age < 4:
    price=0
elif age < 18:
    price=5
elif age < 65:
    price=10
elif age > 65:
    price=5

print("Your admission cost is $"+str(price)+".")

#确定列表非空
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")

