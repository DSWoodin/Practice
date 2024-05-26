# 함수 기본값

def profile(name, age, main_lang):
    print('이름: {0}\t나이: {1}\t주 사용 언어: {2}' \
          .format(name, age, main_lang)) # 탈출문자 (\t)와 줄바꿈 (\) 사용

profile('유재석', 20, '파이썬')
profile('김태호', 25, '자바')

# 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age=17, main_lang='파이썬'): # 기본값을 설정함으로써 입력값이 없을때는 자동으로 기본값이 출력됨
    print('이름: {0}\t나이: {1}\t주 사용 언어: {2}' \
          .format(name, age, main_lang)) 
    
profile('유재석')
profile('김태호')

# 함수 키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name='유재석', main_lang='파이썬', age=20)
profile(main_lang='자바', age=25, name='김태호')