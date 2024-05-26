# 함수 지역변수

gun = 10

def checkpoint(soldiers): # 경계근무
    gun = 20
    gun = gun - soldiers
    print(f'[함수 내] 남은 총 : {gun}')

print(f'전체 총 : {gun}')
checkpoint(2)
print(f'전체 총 : {gun}') # gun = 10 이라는 값이 변하지 않았음 -> gun은 지역변수

# 함수 전역변수

gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun을 사용하겠다는 의미
    gun = gun - soldiers
    print(f'[함수 내] 남은 총 : {gun}')

print(f'전체 총 : {gun}')
checkpoint(2)
print(f'전체 총 : {gun}') # gun = 10 이라는 값을 함수에서 사용함 -> gun을 전역변수로 사용

# 일반적으로 전역변수를 많이 사용하면 코드가 꼬일 확률이 높아지므로 권장되지 않음
# 대부분 함수의 파라미터(입력값)를 넣어서 출력값을 받는 방법을 사용

gun = 10

def checkpoint_ret(gun, soldiers): 
    gun = gun - soldiers
    print(f'[함수 내] 남은 총 : {gun}')
    return gun # 출력값 설정 -> practice13.py

print(f'전체 총 : {gun}')
gun = checkpoint_ret(gun, 2) # 출력값을 받아서 원래 10이였던 gun을 업데이트
print(f'전체 총 : {gun}') 