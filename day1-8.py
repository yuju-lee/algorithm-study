# n (int): 전체 사람 수
# k (int): 큐에서 제거할 순번

from collections import deque

def solution(n: int, k: int) -> str:
    # 1부터 n까지 큐에 넣기
    queue = deque(range(1, n + 1))
    result = []
    
    while queue:  # 큐가 빌 때까지
        # k-1번 만큼 돌면서 k번째 사람이 맨 앞에 오도록 함
        for _ in range(k - 1):
            queue.append(queue.popleft())
        # k번째 사람을 제거하고 결과 리스트에 추가
        result.append(str(queue.popleft()))
    
    # 요세푸스 순열 형식으로 결과 반환
    return f"<{', '.join(result)}>"


n, k = map(int, input().split())
print(solution(n, k))
