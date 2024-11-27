#리스트의 append와 pop 사용 (time complex: O(1))
# 람다 함수를 활용해 연산 로직 정의

import sys
from typing import List

def solution(commands: List[str]) -> List[int]:
    stack = []  # 스택을 리스트로
    results = []
    
    # 스택 연산을 람다 함수로 정의
    operations = {
        'size':  lambda: len(stack),
        'empty': lambda: 1 if not stack else 0,
        'top':   lambda: stack[-1] if stack else -1,
        'pop':   lambda: stack.pop() if stack else -1
    }

    for cmd in commands:
        if cmd.startswith('push'):
            _, num = cmd.split()
            stack.append(int(num))
        else:
            result = operations[cmd]()
            if cmd != 'push':
                results.append(result)
    
    return results

input = sys.stdin.readline
n = int(input())

commands = [input().strip() for _ in range(n)]
results = solution(commands)

print('\n'.join(map(str, results)))