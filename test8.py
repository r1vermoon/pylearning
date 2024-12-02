#break
prompt="\nEnter the name of a city"
prompt+="\n(Enter 'quit' when you are finished)"

while True:
    city=input(prompt)

    if city=='quit':
        break
    else:
        print("I like "+city+"!")

#continue
current_number=0
while current_number<10:
    current_number+=1
    if current_number % 2 == 0:
        continue

    print(current_number)

#while & dic\list
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

while unprinted_designs:
    current_design=unprinted_designs.pop()
    completed_models.append(current_design)

print(completed_models)

# 输入填充字典
responses={}
active=True

while active:
    name=input("what is your name?")
    response=input("which mountain?")

    responses[name]=response
    repeat=input("someone else(yes/no)?")
    if repeat=="no":
        break

for name,response in responses.items():
    print(name+"  "+response)