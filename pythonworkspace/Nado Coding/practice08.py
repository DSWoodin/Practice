# 튜플

# 튜플은 리스트와 사전형과 달리 값 변경 불가능
menu = ('돈까스', '치즈까스')
print(menu[0])
print(menu[1])
# menu.add('생선까스') # 튜플은 값 변경 불가, 오류 발생

# name = '김종국'
# age = 20
# hobby = '코딩'
# print(name, age, hobby)
(name, age, hobby) = ('김종국', 20, '코딩')
print(name, age, hobby)