a = input('첫 번째 숫자를 입력하세요 : ')
b = input('두 번째 숫자를 입력하세요 : ')
print(a + b) # input은 입력값을 문자열로 받음
print('------------------')

a = int(input('첫 번째 숫자를 입력하세요 : '))
b = int(input('두 번째 숫자를 입력하세요 : '))
print(a + b)
print('------------------')

a, b = input('문자열 2개를 공백을 두고 입력하세요 : ').split()
print(a); print(b)
# input.split() 은 공백을 기준으로 분리
# Hello Python을 입력했다면 a = Hello, b = Python 임
print('------------------')

a, b = input('숫자 2개를 공백을 두고 입력하세요 : ').split()
print(int(a) + int(b)) 
# input 값은 문자열이므로 숫자계산을 위해서 변환
print('------------------')

a, b = map(int, input('숫자 2개를 콤마(,)를 넣어 입력하세요 : ').split(','))
print(a + b)
# .split(',')은 입력받은 input 값을 콤마(,) 기준으로 분리
# .split() 안에 분리기준이 되는 문자열을 넣어서 분리할수 있음
# map 함수를 이용해서 미리 문자열을 숫자로 바꿈
print('------------------')

a, b, c = map(int, input('숫자 3개를 공백을 두고 입력하세요 : ').split())
print(a + b + c)
