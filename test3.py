#遍历
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("------------------")

#range
for value in range(2,5):
    print(value)

numbers=list(range(1,5,2))
print(numbers)

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares=[value**2 for value in range(1,11)]
print(squares)
print("------------------")

# [：]
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[1:4]) #不要前1-4
print(players[:4])  #前4
print(players[2:])  #不要前2
print(players[-3:])  #后3

#复制
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)
print("------------------")

#元组
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200, 50) 
print("Original dimensions:") 
for dimension in dimensions: 
    print(dimension)  
dimensions = (400, 100) 
print("\nModified dimensions:") 
for dimension in dimensions: 
    print(dimension)

