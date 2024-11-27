# 스택을 두개로 사용하면 좋다!
# 오른쪽은 글자가 거꾸로 담겨있으니, 리버스해주고 합치면 문자열을 얻을 수 있음

import sys
from typing import List

class Editor:
    #initial
    def __init__(self, initial_text: str):
        self.left_stack: List[str] = list(initial_text) # 커서 기준으로 왼쪽
        self.right_stack: List[str] = [] # 커서 기준으로 오른쪽 
    
    # 커서 이동
    def move_left(self) -> None:
        if self.left_stack:  # 왼쪽 스택이 비어있지 않은 경우
            self.right_stack.append(self.left_stack.pop()) # 이동
    
    def move_right(self) -> None: 
        if self.right_stack:  # 오른쪽 스택이 비어있지 않은 경우 
            self.left_stack.append(self.right_stack.pop())
    
    # 삭제
    def delete_left(self) -> None:
        if self.left_stack:
            self.left_stack.pop()
    
    # 커서 왼쪽에 추가 
    def add_char(self, char: str) -> None:
        self.left_stack.append(char)
    
    def get_text(self) -> str:
        return ''.join(self.left_stack + self.right_stack[::-1])


def solution(initial_text: str, commands: List[str]) -> str:
    editor = Editor(initial_text)
    command_map = {
        'L': editor.move_left,
        'D': editor.move_right,
        'B': editor.delete_left,
    }
    
    for cmd in commands:
        if cmd[0] == 'P':
            editor.add_char(cmd[2]) # 공백있어서 2 
        else:
            command_map[cmd[0]]()
    
    return editor.get_text()


input = sys.stdin.readline
initial_text = input().strip()
m = int(input())

commands = [input().strip() for _ in range(m)]
result = solution(initial_text, commands)
print(result)