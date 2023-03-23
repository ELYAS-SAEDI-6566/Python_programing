print('v2.1',"\n")
with open('names.txt','r') as f:
    lines = []
    for i in f.readlines():
        lines.append(i.replace("\n",""))

with open('selecteds.txt','r') as f:
    selecteds = []
    for i in f.readlines():
        selecteds.append(i.replace("\n",""))
      
import random
def rw():
    global selecteds
    global lines
    global name
    if selecteds :
        name = random.choice(selecteds) 
        selecteds.remove(name)
        with open('selecteds.txt','w') as f:
            f.writelines(i+"\n" for i in selecteds)
    else:
        print('__________________')
        selecteds = [] + lines
        name = random.choice(selecteds) 
        selecteds.remove(name)
        with open('selecteds.txt','w') as f:
            f.writelines(i+"\n" for i in selecteds)

rw()
print(name,"\n")
print('press Enter to see a other name')

while(True):
    input('')
    rw()
    print(name)
