# 표준 입출력

# import sys
# print('Python', 'Java', file=sys.stdout) # 표준 출력
# print('Python', 'Java', file=sys.stderr) # 표준 에러

scores = {'수학':0, '영어':50, '코딩':100} # 시험 성적
for subject, score in scores.items(): # subject(수학,영어,코딩)과 score(0,50,100)를 튜플로 scores.items에 넣기
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=':') 
    # ljust(x): 해당 출력값을 x만큼의 공간을 확보하고 왼쪽(left)에서 부터 출력
    # rjust(x): 해당 출력값을 x만큼의 공간을 확보하고 오른쪽(right)에서 부터 출력

for num in range(1,21):
    # print('대기번호 : ' + str(num))
    print('대기번호 : ' + str(num).zfill(3))
    # zfill(x): 해당 출력값을 x만큼의 공간을 확보하고 값이 없는 공간은 0으로 출력

answer = input('아무 값이나 입력하세요 : ') # input으로 입력한 값은 str(문자열) 형태로 저장됨
print(type(answer))
print('입력하신 값은 ' + answer + '입니다.')