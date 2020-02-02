import math
a,b,x = map(int,input().split())
kagen = (a-1)//x
jougen = b//x
answer = jougen - kagen
print(answer)
