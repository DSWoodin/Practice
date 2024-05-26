# 함수 전달값(입력값), 반환값(출력값)

def open_account():
    print('새로운 계좌가 생성되었습니다.') # 4번 라인까지 실행하면 출력값이 없음
open_account() # 3,4번에서 함수를 정의했고, 5번 라인을 실행하여 함수값이 출력됨

def deposit(balance, money): # 입금
    print(f'입금이 완료되었습니다. 잔액은 {balance + money}원 입니다.')
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금액보다 많으면
        print(f'출금이 완료되었습니다. 잔액은 {balance - money}원 입니다.')
        return balance - money
    else:
        print(f'잔액이 부족하여 출금이 불가합니다. 잔액은 {balance}원 입니다.')
        return balance
    
def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    print(f'수수료는 {commission}원이며, 잔액은 {balance - money - commission}원입니다.')
    return commission, balance - money - commission # 수수료와 잔액을 튜플로 반환
    
balance = 0 # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 300)