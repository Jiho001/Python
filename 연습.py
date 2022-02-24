def group(g):
    for k in range(len(g)):
        ll = g.find(g[k],k+2)
        if ll != -1:
            for m in range(ll-k):
                if g[k+m]!=g[k+m+1]: return 0
    return 1

n=int(input())
cnt = 0
for i in range(n):
    g = input()
    cnt += group(g)
print(cnt)
