H, W = map(int,input().split())
map = [input() for i in range(H)]

def drow(i,j, map = map):
  if j > 0 and map[i][j-1] == "#":
    return "Yes"
  if j < W-1 and map[i][j+1] == "#":
    return "Yes"
  if i > 0 and map[i-1][j] == "#":
    return "Yes"
  if i < H -1 and map[i+1][j] == "#":
    return "Yes"
  return "No"

ans = "Yes"
for i in range(H):
  for j in range(W):
    if map[i][j] == "#":
      ans = drow(i,j)
      if ans == "No":
        print(ans)
        exit()
print(ans)
    
