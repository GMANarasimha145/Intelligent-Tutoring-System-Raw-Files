import math
def isPrime(num):
    if num==1:
        return False
    if num==2:
        return True
    for i in range(2,num):
        if num%i==0:
            return False
    return True

lt = list(map(int,input().split(" ")))
n=len(lt)
fmax,smax = float('-inf'),float('-inf')
fmin,smin = float('inf'),float('inf')
new_lt = []
for i in lt:
    if isPrime(i):
        new_lt.append(i)
print(new_lt)

new_n = len(new_lt)
for i in range(new_n):
    if new_lt[i]>fmax:
        smax = fmax
        fmax = new_lt[i]
    elif new_lt[i]>smax and new_lt[i]!=fmax:
        smax = new_lt[i]
        
    if new_lt[i]<fmin:
        smin = fmin
        fmin = new_lt[i]
    elif new_lt[i]<smin and new_lt[i]!=fmin:
        smin = new_lt[i]
        
print(fmax,smax,fmin,smin)

count=0
x, y = map(int,input().split(" "))
for i in range(x,y+1):
    if isPrime(i):
        print("PN: ",i)
        count+=1