A,B,C = map(int, input().split())
ans_list = []
count = 1
while True:
  div_num = A*count
  ans = div_num % B
  if ans in ans_list:
    break
  else:
    ans_list.append(ans)
  count += 1
if C in ans_list:
  print("YES")
else:
  print("NO")
