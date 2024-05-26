# 파일 입출력

score_file = open('practice19.txt', 'w', encoding='utf8') 
# open(생성할 파일 이름, 'w':이 파일은 쓰기(write) 목적으로 사용하겠음
#      encoding='utf8': 한글 정보를 받기 위해)
print('수학 : 0', file=score_file)
print('영어 : 50', file=score_file) # 파일에 값을 넣는 방법 1
# score_file을 쓰기 목적으로 열고 수학과 영어 점수를 쓴뒤 파일 닫기
score_file.close() # 파일을 open 했으면 close 해야됨
# 현재 pythonworkspace 파일에서 작업을 하고 있으므로 여기 안에 텍스트 파일이 생성됨

score_file = open('practice19.txt', 'a', encoding='utf8')
# 'w'는 덮어쓰기 개념인 반면, 'a'는 이어쓰기(append) 
# 기존 file 안의 자료를 훼손하지 않고 덧붙여서 씀
score_file.write('과학 : 80') # 파일에 값을 넣는 방법 2
score_file.write('\n코딩 : 100') # 이 방법은 print 방법과 달리 줄바꿈을 자동으로 해주지 않음
score_file.close()

score_file = open('practice19.txt', 'r', encoding='utf8') # 'r': 파일을 읽기(read) 목적으로 사용
print(score_file.read()) # score_file의 모든내용()을 읽어오겠다
score_file.close()

score_file = open('practice19.txt', 'r', encoding='utf8')
print(score_file.readline()) # readline: 한 줄씩 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline()) # print는 자동으로 줄바꿈을 해주기 때문에 공백 줄이 하나씩 생김
print(score_file.readline(), end='') # 줄바꿈을 안하고 싶으면 end='' 구문 사용
print(score_file.readline()) 
score_file.close()

score_file = open('practice19.txt', 'r', encoding='utf8')
while True:
    line = score_file.readline()
    if not line:
        break # 파일이 몇 줄일지 모를때 반복문으로 읽어오기
    print(line, end='')
score_file.close()

score_file = open('practice19.txt', 'r', encoding='utf8')
lines = score_file.readlines() # 모든 라인을 가지고 와서 list로 저장
for line in lines:
    print(line, end='') # 읽어온 모든 라인을 한줄씩 프린트
score_file.close()