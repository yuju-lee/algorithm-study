# n = int(input())
# btn = list(map(int, input().split()))
# stucnt = int(input())
# info = []
# for i in range(stucnt):
#     sex, cnt = map(int, input().split())
    
#     #남자여자 분기
#     if sex == 1: #남자일 경우
#         manbtn = [] #배수 만들기
#         for m in range(0, len(btn)+1, cnt):
#             if 1 < m:
#                 manbtn.append(m)
#         # 스위치를 자기가 받은 배수의 스위치 번호 상태 바꾸기
#         for j in range(len(manbtn)):
#             if btn[manbtn[j]-1] == 1: btn[manbtn[j]-1]=0
#             else: btn[manbtn[j]-1]=1

#     #여자일 경우
#     else: #좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아 상태 바꿈
#         #우선 받은 번호의 버튼 바꾸기
#         center = cnt-1
#         if btn[center] == 1: btn[center] = 0
#         else: btn[center] = 1
            
#         # 처음 마지막 예외처리
#         #받은 번호가 스위치의 처음이자 마지막이 아닐 경우
#         k=1
#         while 0 <= center-k and center+k < len(btn):
#             if btn[center - k] == btn[center + k]:
#                 btn[center - k] = 1 - btn[center - k]
#                 btn[center + k] = 1 - btn[center + k]
#             else:
#                 break
#             k += 1
            
# for i in range(0, len(btn), 20):
#     print(' '.join(map(str, btn[i:i+20])))


n = int(input())
btn = list(map(int, input().split()))
stucnt = int(input())

#학생수만큼 반복
for i in range(stucnt):
    #성별과 받은 수 입력받기
    sex, cnt = map(int, input().split())

    # 남자일 경우
    if sex == 1:
        # 스위치를 자기가 받은 배수의 스위치 번호 상태 바꾸기
        #받은수-1부터 n까지, 받은수만큼 건너뛰기
        for j in range(cnt - 1, n, cnt):
            btn[j] = 1 - btn[j]

    # 여자일 경우
    else: #좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아 상태 바꿈
        #기준값은? (인덱스는 0부터라 -1)
        center = cnt - 1
        #우선 받은 번호의 버튼 바꾸기
        btn[center] = 1 - btn[center]

        # 좌우 대칭 구간 찾기
        k = 1
        # 처음 마지막 예외처리
        #받은 번호가 스위치의 처음이자 마지막이 아닐 경우
        
        #
        while 0 <= center - k and center + k < n:
            if btn[center - k] == btn[center + k]:
                btn[center - k] = 1 - btn[center - k]
                btn[center + k] = 1 - btn[center + k]
            else:
                break
            k += 1

# 20개씩 끊어서 결과 출력 
for i in range(0, len(btn), 20):
    print(' '.join(map(str, btn[i:i+20])))