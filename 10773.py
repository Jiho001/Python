t = int(input())
wh = []
for i in range(t):
    a = int(input())
    if a == 0: wh.pop()
    else: wh.append(a)
print(sum(wh) if len(wh)>0 else 0)