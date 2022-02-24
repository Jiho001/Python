a=input()
cnt = 0
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in cro:
    a = a.replace(i,'!')
print(len(a))