"""
3-1. 숫자 카드 게임
1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
   최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
"""

# N, M을 공백을 기준으로 입력 받기
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))

    # 입력받은 행에서의 최솟값을 찾기
    min_number = min(data)

    # 현재까지 입력받은 행에서의 최솟값들 중 최댓값 answer에 저장하기
    result = max(result, min_number)

# 출력
print(result)

# 시간복잡도: O(N^2)

"""
3-2. 2중 반복문으로 풀기
"""

# N, M을 공백을 기준으로 입력 받기
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))

    # 입력받은 행에서의 최솟값을 찾기
    min_number = 10001
    for a in data:
        min_number = min(min_number, a)
    # 현재까지 입력받은 행에서의 최솟값들 중 최댓값 answer에 저장하기
    result = max(result, min_number)

# 출력
print(result)

# 시간복잡도: O(N^2)