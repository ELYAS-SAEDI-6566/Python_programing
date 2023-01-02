value = str(input())
nxk = value.split()
n = int(nxk[0])
x = int(nxk[1])
k = int(nxk[2])
TVs = []
for i in range(n):
    TVs.append(input())
pointer = x-1
for i in range(k):
    if pointer == n-1:
        pointer = 0
    else:
        pointer += 1
print(TVs[pointer])