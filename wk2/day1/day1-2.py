#32ms
import sys

input = sys.stdin.readline
cnt = int(input())
ls = []

for i in range(cnt):
    n = list(map(str, input().split()))

    for j in range(len(n)):
        rev = list(reversed(n))
        result = " ".join(rev)

    print(f"Case #{i+1}: {result}")
