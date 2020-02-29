#print("hello ")
#name='adea '
#print(name.title()+"\npython")
#print(name.rstrip())
#3**2
#age=12
#print("wo"+str(age))
#2/29
#import this
languages = ['java','c','php','python','.net']

print(languages[0])
print(languages[-1])
languages.append('c++')
languages.insert(1,'go')

for lan in languages:
    print(lan)
    print("is a good language")
print('bye~')

for value in range(1,5):
    print(value)
print(list(range(1,5,2)))
print(3**2)

cal = [calu*2 for calu in range(1,11)]
print(cal)
print(cal[0:2])
print(cal[:6])
print(cal[-1:])
copycal = cal[:]
print(copycal)
dim = (10,5)
if dim:
    for di in dim:
        if 7 not in dim:
            if 5 in dim:
                if di != 6 and di == 10:
                    print("hhh"+str(di))
        elif 5 in dim:
            print("")
        else:
            print("else")
print(dim[0])
#del languages[3]
#print(languages)
#popvalue = languages.pop(1)
#languages.remove('.net')
# languages.sort(reverse=True)
#print(sorted(languages))
#print(languages)
#print(popvalue)
#print(len(languages))