from sys import stdin

T = int(stdin.readline())
for i in range(T):
    A, B = map(int, stdin.readline().rstrip().split())
    print("Case {0}: {1}".format(i+1, A+B))
