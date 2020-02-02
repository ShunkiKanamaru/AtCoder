N, Q = map(int,input().split())
tree_list = []
count_list = [0]*N

def make_tree(a,b):
  if len(tree_list) == 0:
    tree_list.append([a,b])
    tree_list.append([b])
  else:
    for i in range(len(tree_list)):
      if a in tree_list[i]:
        tree_list[i].append(b)
      if i == len(tree_list)-1:
        tree_list.append([b])
def count(num,x):
  for i in tree_list[num]:
    count_list[i-1] +=x
for i in range(N-1):
  a,b = map(int,input().split())

  make_tree(a,b)
for i in range(Q):
  p,x = map(int,input().split())
  tree_num = tree_list[0].index(p)
  count(tree_num,x)
count_list = [str(i) for i in count_list]
print(" ".join(count_list))
