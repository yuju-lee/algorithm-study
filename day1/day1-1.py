# 줄이 늘어날수록 별을 1개씩 더함 
# 1번 줄 1개, 2번 줄 2개 ... n번 줄은 n+1개

n = int(input("")) #input
for i in range(n):
    print("*"*(i+1)) #i+1만큼 출력