N = int(input())
ans_list =[]
for i in range(N):
    ans_list.append(int(input()))
max = max(ans_list)
ans = 0
for i in ans_list:
    ans = ans + i
ans = ans-int(max/2)
print(ans)
