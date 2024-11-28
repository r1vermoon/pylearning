pizza={
    'crust': 'thick', 
    'toppings': ['mushrooms', 'extra cheese'],
}

for topping in pizza['toppings']:
    print("\t"+topping)

for topping in ["a","b"]:
    print("\t"+topping)

for topping in "a","b":
    print("\t"+topping)

users = { 
    'aeinstein':{ 'first': 'albert', 
                  'last': 'einstein', 
                  'location': 'princeton', 
                }, 
      'mcurie': { 'first': 'marie', 
                 'last': 'curie', 
                 'location': 'paris', }, 
                   }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last'] 
    location = user_info['location']

    print("\tFull name: " + full_name.title()) 
    print("\tLocation: " + location.title())

cats={
    'miaomiao':{'color':"white",
                'location':'china',
    },
    'xiaomei':{'color':'black',
               'location':'America'
            }
}

for catname,catinfo in cats.items():
    print("\ncatname: " + catname)
    color=catinfo['color']

    print("\tcolor: " + color) 