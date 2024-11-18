#列表元素表示
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title()) #首字母大写
print(bicycles[-1])

message="My first bicycle was a "+bicycles[0].title()+"."
print(message)
print("------------------")

#列表元素改 增append 插insert 删del 
motorcycles=['honda','yamaha','suzuki']
bicycles[0]='ducati'
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
del motorcycles[0]
print(motorcycles)

#pop()
motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(0)
print("My first motorcycle is "+first_owned+'.')
print(motorcycles)
print("------------------")

#组织列表
cars=['bnw','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)
print(sorted(cars))  #临时改变
cars.reverse()  #反转
print(cars)
print(len(cars))

print(cars[-1])
