# for, while

for waiting_num in [0,1,2,3,4]: # 0,1,2,3,4
    print('대기번호 : {0}'.format(waiting_num))

for waiting_num in range(5): # 0,1,2,3,4
    print('대기번호 : {0}'.format(waiting_num))

for waiting_num in range(1,6): # 1,2,3,4,5
    print('대기번호 : {0}'.format(waiting_num))

starbucks = ['1', '2', '3']
for customer in starbucks:
    print('주문번호 {0}번 손님, 커피 나왔습니다.'.format(customer))

customer = '1'
person = 'Unknown'

while person != customer:
    print('주문번호 {0}번 손님, 커피 나왔습니다.'.format(customer))
    person = input('주문번호가 어떻게 되세요? : ')