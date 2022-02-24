<<<<<<< HEAD
h, m = map(int,input().split())
c = int(input())
if c/60 > 1:
    h += c//60
    if m+(c%60) >= 60:
        h += 1
        m = (m+(c%60) - 60)
    else: m = c%60
else:
    if m+c>=60:
        m = (m+c) - 60
        h+=1
    else:
        m += c
if h >=24:
    h = h - 24
print(h,m)
=======
n, m = map(int,input().split())
lan = [int(input()) for _ in range(n)]

so, dae = 1, max(lan)
while so <= dae:
    mid = (so + dae)//2
    cnt = 0
    for i in lan:
        cnt += i//mid 
    if cnt >= m: so = mid + 1
    else: dae = mid -1
print(dae)

>>>>>>> e1ae18ce7eecd5236c25bb33bc870d5e244ba255
