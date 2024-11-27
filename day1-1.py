#time complexity: O(n) + O(n) + O(n) = O(n)
import sys

# 빠른 입력을 위한 sys.stdin.readline 사용
input = sys.stdin.readline

def result():
    n = int(input()) # 건물의 개수 n
    h = [] # 건물 높이를 저장할 리스트
    cnt = 0 # 보이는 건물 수

    for i in range(n):
        s = int(input())
        h.append(s)

    # 오른쪽에서 왼쪽으로 건물을 확인하기 위해 입력된 값 reversed
    # 입력된 높이를 뒤집은 리스트 hr
    hr = list(reversed(h))

    # 마지막 건물 기준
    last = h[-1]
    highest = 0

    # 뒤집힌 리스트 hr을 순회하며 오른쪽에서 왼쪽으로 볼 수 있는 건물을 확인
    for j in hr:
        if last <= j and highest < j:
            cnt += 1  # 보이는 건물 개수 증가
            highest = j  # 최고 높이 갱신

    return cnt

print(result())