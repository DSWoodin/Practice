import numpy as np

# ndarray는 문자열과 정수가 섞인 배열을 생성하면
# 모든 요소를 문자열로 변환하고, 정렬 같은 연산도 문자열 기준으로
a=np.array([400,52,'tiger','24',230])
print(a)
print(type(a))
print(a.shape)
a.sort()
print(a)

# Numpy의 ndarray 객체가 제공하는 주요 멤버 함수
    # min: 배열의 최솟값을 반환합니다.
    # max: 배열의 최댓값을 반환합니다.
    # argmin: 배열의 최솟값이 있는 인덱스를 반환합니다.
    # argmax: 배열의 최댓값이 있는 인덱스를 반환합니다.
    # mean: 배열의 평균값을 반환합니다.
    # sum: 배열의 모든 요소의 합을 반환합니다.
    # cumsum: 배열의 누적 합을 반환합니다.
    # prod: 배열의 모든 요소의 곱을 반환합니다.
    # cumprod: 배열의 누적 곱을 반환합니다.

# 10개의 실수를 가진 ndarray 객체 생성
arr = np.array([1.5, 2.3, 3.7, 4.1, 5.9, 6.0, 7.4, 8.2, 9.0, 10.5])

# 각 함수들을 적용하고 결과 출력
print("Array:", arr)
print("Min:", arr.min())
print("Max:", arr.max())
print("Argmin (index of min):", arr.argmin())
print("Argmax (index of max):", arr.argmax())
print("Mean:", arr.mean())
print("Sum:", arr.sum())
print("Cumsum:", arr.cumsum())
print("Prod:", arr.prod())
print("Cumprod:", arr.cumprod())