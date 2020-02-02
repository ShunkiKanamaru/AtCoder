A,B,C,D = map(int, input().split())
if min(B,D) <= max(A,C):
  print(0)
else:
  print(min(B,D)-max(A,C))
