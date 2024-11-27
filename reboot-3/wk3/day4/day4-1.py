#40ms
def findcomp(num1, num2):
    combined = []
    for i in range(len(num1)):
        combined.append(int(num1[i]))
        combined.append(int(num2[i]))

    dp = [combined]

    while len(dp[-1]) > 2:
        current = dp[-1]
        next = []
        for i in range(len(current) - 1):
            next.append((current[i] + current[i + 1]) % 10)
        dp.append(next)

    final = dp[-1]
    return f"{final[0]}{final[1]}"

num1 = input().strip()
num2 = input().strip()

result = findcomp(num1, num2)
print(result)
