# 리스트

subway = ['A','B','C']
print(subway.index('B')) 
# 리스트에서 특정 개체 위치 찾기

subway.append('D') # 리스트 맨 뒤에 삽입
print(subway)

subway.insert(1,'E') # 리스트 원하는 곳에 삽입
print(subway)

subway.pop() # 리스트 맨 뒤에 삭제
print(subway)

subway.pop()
print(subway)

subway.append('A')
print(subway)
print(subway.count('A')) 
# 리스트에서 특정 개체 갯수 세기

num_list = [5,2,4,3,1]
num_list.sort() # 오름차순 정렬
print(num_list)

num_list.reverse # 순서 뒤집기
print(num_list)

num_list.clear() # 모두 지우기
print(num_list)

num_list = [5,2,4,3,1]
mix_list = ['A', 20, True] # 다양한 자료형 함께 사용가능
print(mix_list)
num_list.extend(mix_list) # 리스트 확장
print(num_list)