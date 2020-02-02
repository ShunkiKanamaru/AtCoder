N = int(input())
button_list =[]
for i in range(1,N+1):
  button_list.append(int(input()))

count = 0
dest = 1
for i in range(N):
    dest = button_list[dest - 1]
    count +=1
    if dest == 2:
        break;
if count == N:
    print(-1)
else:
    print(count)
