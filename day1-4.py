# O(1) 시간 복잡도를 가진 deque 사용
# deque는 양쪽 끝에서 삽입과 삭제가 가능한 자료구조로, 큐나 스택을 구현할 때 사용

from collections import deque
import sys

def process_commands(commands):
    queue = deque()  
    results = []
    
    empty_check = lambda: 1 if not queue else 0
    
    command_map = {
        'size': lambda: len(queue),
        'empty': empty_check,
        'front': lambda: queue[0] if queue else -1,
        'back': lambda: queue[-1] if queue else -1
    }

    for command in commands:
        if command.startswith('push'):  # push 명령 처리
            queue.append(int(command.split()[1]))
            continue
            
        if command == 'pop':  # pop 명령 처리
            results.append(queue.popleft() if queue else -1)
            continue
            
        # 나머지 명령어들 처리
        results.append(command_map[command]())
    
    return results

def main():
    input = sys.stdin.readline
    n = int(input())
    commands = [input().strip() for _ in range(n)]
    output = process_commands(commands)
    print('\n'.join(map(str, output)))

if __name__ == "__main__":
    main()