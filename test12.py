#文件读取
with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents.rstrip())

filename='pi_digits.txt'

#逐行读取
with open(filename) as file:
    for element in file:
        print(element)

with open(filename) as file:
    for element in file:
        print(element.rstrip())

#读取行为列表,注意readline()和readlines()不同
with open(filename) as file:
    lines=file.readlines()

for line in lines:
    print(line.rstrip())

pi_string=''
for line in lines:
    pi_string+=line.strip()

print(pi_string)
print(len(pi_string))


#文件写入
filename='programming.txt'
with open(filename,'w') as file:
    file.write("I love programming.\n")
    file.write("really?\n")

#续写
with open(filename,'a') as file:
    file.write("I also love creating apps.")

#异常
try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

filename='alice.txt'

try:
    with open(filename) as file1:
        contents=file1
except FileNotFoundError:
    print("Sorry,the file does not exist.")
else:
    num_words=len(contents.split())
    print(num_words)
