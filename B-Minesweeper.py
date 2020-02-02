H,W = map(int,input().split())
box_list = [input() for i in range(H)]

def search(i,j,box_list = box_list):
  count = 0
  if j > 0 and box_list[i][j-1] == "#":
    count += 1
  if j < W-1 and box_list[i][j+1] == "#":
    count += 1
  if i > 0 and box_list[i-1][j] == "#":
    count += 1
  if i < H-1 and box_list[i+1][j] == "#":
    count += 1
  if j > 0 and i < H-1 and box_list[i+1][j-1] == "#":
    count += 1
  if j < W-1 and i < H-1 and box_list[i+1][j+1] == "#":
    count += 1
  if j > 0 and i > 0 and box_list[i-1][j-1] == "#":
    count += 1
  if j < W-1 and i > 0 and box_list[i-1][j+1] == "#":
    count += 1
  return count


for i in range(H):
  answer = ""
  for j in range(W):
    if box_list[i][j] != "#":
      answer += str(search(i,j))
    else:
      answer += "#"
  print(answer)
