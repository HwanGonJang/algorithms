"""
6-1. 위에서 아래로
하나의 수열에는 다양한 수가 존재하며, 이런 큰 수는 크기와 상관 없이 무작위로 주어진다.
이 수를 큰수 부터 작은 수까지 내림차순으로 정렬하면하라. 수열을 내림차순으로 정렬하는 프로그램을 만드시오.
"""
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

# 시간복잡도: O(NlogN)
# 기본 정렬 라이브러리의 시간복잡도는 O(NlogN)을 보장한다.