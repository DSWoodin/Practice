# 집합(set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)
print('---------------')
java = {'유재석','김태호','양세형'} # set 자료 넣기 방법 1
python = set(['유재석','박명수']) # set 자료 넣기 방법 2

# 교집합 (java, python 둘다 가능)
print(java & python)
print(java.intersection(python))

# 합집합 (java, python 하나라도 가능)
print(java | python)
print(java.union(python))

# 차집합 (java 가능, python 불가능)
print(java - python)
print(java.difference(python))

# 값 추가, 값 제거
python.add('김태호')
print(python)
java.remove('김태호')
print(java)