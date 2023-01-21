t = input()
t = t.split()
a = int(t[0])
b = int(t[1])
if a == 0:
    h = 0
else:
    h = 12-a
if b == 0:
    m = 0
else:
    m = 60-b
if len(str(h)) == 1 :
    h = "0"+str(h)
if len(str(m)) == 1 :
    m = "0"+str(m)
print(f"{h}:{m}")