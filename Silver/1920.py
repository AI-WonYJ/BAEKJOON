import sys

N = int(sys.stdin.readline())
N_list = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for m in M_list:
  # print(1) if m in N_list else print(0)
  if m in N_list:
    print(1)
  else:
    print(0)