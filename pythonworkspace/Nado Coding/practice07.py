# 사전형

cabinet = {3:'A', 100:'E'}
print(cabinet[3]) # 사전형 자료 찾기 방법 1
print(cabinet[100])
print(cabinet.get(3)) # 사전형 자료 찾기 방법 2

# print(cabinet[5]) 
# 방법 1은 없는 값을 찾게 하면 오류 발생
print(cabinet.get(5))
# 방법 2는 없는 값을 찾게 하면 None 반환
print(cabinet.get(5,'사용 가능'))
# 값이 없으면 None 말고 원하는 값을 반환하게 할수 있음
print(3 in cabinet) # 해당 값이 있는지 찾기 -> True
print(5 in cabinet) # False

cabinet = {'A-3':'유재석', 'B-100':'김태호'} # 문자형 가능
print(cabinet['A-3'])
print(cabinet['B-100'])

print(cabinet)
cabinet['A-3'] = '김종국' # 값 추가(변경)
cabinet['C-20'] = '조세호'
print(cabinet)
del cabinet['A-3'] # 값 삭제
print(cabinet)

print(cabinet.keys()) # key 들만 출력
print(cabinet.values()) # value 들만 출력
print(cabinet.items()) # key,value 쌍으로 출력
cabinet.clear() # 모두 지우기
print(cabinet)