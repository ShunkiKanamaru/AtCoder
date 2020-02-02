N,K = map(int,input().split())
pan = "P"
for i in range(N):
    pan = "B" + pan + "P" + pan + "B"
print(pan)
