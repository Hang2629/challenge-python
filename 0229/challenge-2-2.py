def greet_user():
    print("11")

greet_user()

def getanimal(color='red',name=''):
    if name:
        print(name)
    return color

col = getanimal('wangcai')
print(col)

def makepizzas(*tris,):
    print(tris)

makepizzas('mushrooms','greencpos')

def infos(clo,**infos):
    print(str(clo)+","+str(infos))

infos("green",location="chinese",fields="computer")
