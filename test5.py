#字典
alien_0={'color':'green','points':5}
print(alien_0['color'])

# 添加
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#修改
alien_0['color'] ='yellow'
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

if alien_0['speed'] == 'slow': 
    x_increment = 1 
elif alien_0['speed'] == 'medium': 
    x_increment = 2 
else: 
    x_increment = 3  

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(alien_0['x_position'])

#删除
del alien_0['speed']
print(alien_0)

#遍历
user_0 = { 'username': 'efermi', 'first': 'enrico', 'last': 'fermi', }
for key,value in user_0.items():
    print("\nkey: "+ key)
    print("\nvalue: "+ value)

for key in user_0.keys(): 
    print(key.title())

#嵌套
alien_0 = {'color': 'green', 'points': 5} 
alien_1 = {'color': 'yellow', 'points': 10} 
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens: print(alien)