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
