# text (str): 원본 텍스트
# bomb (str): 폭탄 문자
def solve_string_explosion(text, bomb) -> str:
    stack = []
    bomb_len = len(bomb)
    last_char = bomb[-1]  # 폭발 문자열의 마지막 문자 / 마지막 문자는 검사 안하게끔
    
    for char in text:
        stack.append(char)
        
        # 현재 문자가 폭발 문자열의 마지막 문자와 같고
        # 스택의 길이가 폭발 문자열 길이보다 길 때만 검사
        if char == last_char and len(stack) >= bomb_len:
            # 스택의 마지막 부분이 폭발 문자열과 일치하는지 확인
            if ''.join(stack[-bomb_len:]) == bomb:
                # 폭발 문자열 길이만큼 스택에서 제거
                del stack[-bomb_len:]
    
    # 남은 문자들 리턴
    return ''.join(stack) if stack else "FRULA"

def main():
    text = input().strip()
    bomb = input().strip()
    
    result = solve_string_explosion(text, bomb)
    print(result)

if __name__ == "__main__":
    main()