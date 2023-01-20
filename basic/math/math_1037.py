# 1037
import sys

n = int(sys.stdin.readline())

div = sorted(list(map(int, sys.stdin.readline().split())))
result = div[0] * div[-1]

print(result)