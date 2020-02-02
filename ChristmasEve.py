N,K = map(int,input().split())
tree_list = [int(input()) for _ in range(N)]
tree_list = sorted(tree_list)
ans = 10**9
for i in range(N-K+1):
    compare = tree_list[i+K-1]-tree_list[i]
    if ans > compare:
        ans = compare
print(ans)
