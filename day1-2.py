# time complexity: O(cnt * m) 
# cnt: 입력값 count, m: 입력값 길이

import sys

input = sys.stdin.readline
cnt = int(input())
ls = []

for i in range(cnt):
    n = list(map(str, input().split())) # 한 줄을 입력받아 공백으로 나눈 문자열 리스트 생성
    rev = list(reversed(n)) # 문자열 리스트 뒤집기
    result = " ".join(rev) # 뒤집은 리스트를 문자열로 변환
    print(f"Case #{i+1}: {result}")