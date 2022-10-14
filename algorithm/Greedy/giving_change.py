"""
1. 거스름돈
거스름돈으로 사용한 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소의 개수를 구하여라.
"""

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

# 시간복잡도 O(K)