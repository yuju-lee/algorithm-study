# time complexity: (O(n))*(O(log(n))) = O(n log(n))

def solution(x):
    cnt = 0

    while len(x) > 1:
        x = str(sum(map(int, x))) # map 함수를 이용해서 x의 각 자리수를 int로 변환하고, sum으로 합산
        cnt += 1

    # 최종 변환된 숫자가 3의 배수인지 확인
    if int(x) % 3 == 0:
        result = "YES" 
    else:
        result = "NO"
    
    return cnt, result

x = input().strip()
count, result = solution(x)

print(count)
print(result)