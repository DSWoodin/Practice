print(1, 2, 3)
print(1, 2, 3, sep= '') # sep에 비어있는 문자열 지정
print(1, 2, 3, sep= ', ') # sep에 콤마와 공백을 지정
print(1920, 1080, sep= 'x') # sep에 x를 지정
# print로 여러 값을 출력할 때 sep을 이용하여 값사이에 들어갈 문자 지정가능
print('------------------')

print(1, 2, 3, sep= '\n') # \n은 개행(줄바꿈) 문자임
print('1\n2\n3') # 123이라는 문자열에 개행 문자를 넣어 줄바꿈
print('1\t2\t3') # \t는 탭 문자, 여러칸을 띄우는 키보드 탭키와 같은 기능
print('------------------')

print(1, end= '') # end는 sep의 반대 개념
print(2, end= '') # end 뒤에 비어있는 문자열을 지정하여 다음 출력이 바로 뒤에 오게 됨
print(3)
print('------------------')

year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59
print(year, month, day, sep= '/', end= ' ')
print(hour, minute, second, sep= ':')