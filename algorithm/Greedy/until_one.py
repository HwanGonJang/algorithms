"""
# 4-1. 1이 될 떄 까지
1. N에서 1을 뺀다.
2. N을 K로 나눈다.(N이 K로 나누어 떨어질때만 가능)
위의 연산 2개를 반복적으로 사용해서(순서 상관 없음) N을 1로 만들어라.
단, 최소의 연산 횟수를 사용해라.
"""

# N, K을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)

# 시간복잡도: O(N^2)

"""
4-2. 한 번에 빼기
"""

# N, K 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)