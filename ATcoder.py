N = input()
answer_list = []
answer = 0

for i in range(len(N)):
  if N[i] == "A" or N[i] == "T" or N[i] == "C" or N[i] == "G":
    answer += 1
  else:
    answer_list.append(answer)
    answer = 0
  if i+1 == len(N):
    answer_list.append(answer)
print(max(answer_list))
