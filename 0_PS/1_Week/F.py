import sys
from collections import Counter
N_list = [0]*6

A = str(sys.stdin.readline().rstrip())
B_list = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(0, len(B_list)):
  N_list[B_list[i]-1] += 1

count_list = []
for k in range(0, len(N_list)):
  if N_list[k] != 0:
    count_list.append([k+1, N_list[k]])

count_list.sort(key=lambda x : x[1])
count_list.reverse()

result = [0]*12
for j in range(0, len(A)):
  if A[j] == "Y":
    if j <= 5:  # solved
      result[j] = (N_list[j]+2)*(j+1)
    elif j == 6: # solved
      if count_list[0][1] >= 2:
        result[j] = count_list[0][0] * 4
    elif j == 7:
      if len(count_list) == 1:
        if count_list[0][0] == 6:
          result[j] = count_list[0][0]*3 + 5*2
        else:
          result[j] = count_list[0][0]*3 + 6*2
      elif len(count_list) == 2:
        if count_list[0][1] == 1:
          result[j] = count_list[0][0]*(count_list[0][1]+1) + count_list[1][0]*(count_list[1][1]+1)
        elif count_list[0][1] == 2:
          result[j] = count_list[0][0]*count_list[0][1] + count_list[1][0]*(count_list[1][1]+2)
    elif j == 8:
      if N_list[5] == 0 and len(count_list) == 3:
        result[j] = 30
    elif j == 9:
      if N_list[0] == 0 and len(count_list) == 3:
        result[j] = 30
    elif j == 10:
      if len(count_list) == 1:
        result[j] = 50
    elif j == 11:
      sum = 0
      for k in range(0, len(count_list)):
        sum += count_list[k][0]*count_list[k][1]
      result[j] = sum + 6*2

print(max(result))