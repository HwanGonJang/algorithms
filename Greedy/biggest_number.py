"""
2-1. 큰 수의 법칙
동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 방법이다.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

예를 들어 순서대로 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때, M이 8이고 K가 3이라고 가정하자.
이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5인 46이 된다.
단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.

배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.
"""

# n, m, k = map(int, input().split())        # n, m, k
#
# data = list(map(int, input().split()))     # data 리스트
#
# data.sort()
# first = data[n - 1]                        # 가장 큰 값
# second = data[n - 2]                       # 두번째로 큰 값
#
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
#
# print(result)

# 시간복잡도: O(N^2)

"""
2-2. 반복되는 수열로 풀기
가장 큰 수가 더해지는 횟수: int(M / (K + 1)) * K + M % (k + 1) 
"""

n, m, k = map(int, input().split())        # n, m, k

data = list(map(int, input().split()))     # data 리스트

data.sort()
first = data[n - 1]                        # 가장 큰 값
second = data[n - 2]                       # 두번째로 큰 값

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)

# 시간복잡도:O(N) -> 정렬