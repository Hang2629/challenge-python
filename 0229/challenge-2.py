alien_0 = {'color':'green','name':'alien',"age":1000}
print(alien_0['age'])
alien_0['x_position']= 0
alien_0['age']=100
del alien_0['age']
print(alien_0)
favorite_languages = {
'jen': 'python',
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for key,value in favorite_languages.items():
    print("key:"+key)
    print("value:"+value)

for key in favorite_languages.keys():
    print(key)

for value in favorite_languages.values():
    print(value)

for key in sorted(favorite_languages.keys()):
    print(key)

for key in set(favorite_languages.keys()):
    print("---------"+key)

favorite_food1 = {
    'name': 'potato',
    'color': 'yellow'
}
favorite_food2 = {
    'name': 'potato2',
    'color': 'yellow'
}
favorite_food3 = {
    'name': 'potato3',
    'color': 'yellow'
}

favorites = [favorite_food1,favorite_food2,favorite_food3]
for key in favorites[:2]:
    print("favorites[2]:"+str(key))

for a in favorites[0:2]:
    print(a)

users = {
    'chinese': {
        'name':'zhagnsan',
        'age':'12'
    },
    'foreign':{
        'name': 'mary',
        'age': '2'
    }
}

for nation,info in users.items():
    print("nation:"+nation+",info:")
    print("name:"+info['name']+",value:"+info['age'])

#message = input("tell me who do u like")
#print(message)

current_number = 1
while current_number <=5:
    print(current_number)
    current_number +=1

# while favorite_food1:
#    print(favorite_food1.keys())


