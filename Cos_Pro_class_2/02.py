x = 10
print(x)
x, y, z = None, 20, 30
print(x, y, z)
print('------------------')

a, b = 40, 50
x, y = a, b
print(x, y)
print('------------------')

hello1 = '''Hello world!
안녕하세요
Python'''
print(hello1)
print(len(hello1))
print('------------------')

print('Hello, "python"')
print('Hello, \'python\'') 
# 작은따음표 안에 작은따음표 넣기
print('------------------')

hello = 'Hello,'
world = 'world!'
print(hello + world)
print(hello * 3)
print(hello + str(1.5) + ',' + str(10)) 
#str 함수는 숫자(정수, 실수)를 문자열로 변환
print('------------------')

s = 'hello python'
print('s의 길이는 ' + str(len(s)) + '입니다')