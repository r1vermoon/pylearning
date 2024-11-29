#input()

name=input("Please enter your name:")
print("Hello,"+name+"!")

prompt = "If you tell us who you are, we can personalize the messages you see." 
prompt += "\nWhat is your first name? "  
name = input(prompt) 

print("\nHello, " + name + "!")

#int()类型转换
height = input("How tall are you, in inches? ") 
height = int(height)

print(height+1)

#while()
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1

prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. "  
message = "" 
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit': 
        print(message)