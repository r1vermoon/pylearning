from test15 import formatted_name

print("Enter your name,enter 'q' to exist.")
while True:
    first_name=input("give me a first name:")
    if first_name=='q':
        break
    last_name=input("give me a last name:")
    if last_name=='q':
        break
    middle_name=input("give me a middle name:")
    if middle_name=='q':
        break

    full=formatted_name(first_name,last_name,middle_name)
    print(full)