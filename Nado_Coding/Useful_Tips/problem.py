# 참조 강의: https://www.youtube.com/watch?v=LZQC9mEzdtk&list=PLMsa_0kAjjrfYDhzNFLqB8XhSOI0UoIWf&index=5
# 참조 강의: https://www.youtube.com/watch?v=_1HM6MJMYPw&list=PLMsa_0kAjjrfYDhzNFLqB8XhSOI0UoIWf&index=6
# 참조 강의: https://www.youtube.com/watch?v=PEtjVQa_LEA

# 코딩을 하다가 문제가 발생할 때 해결방법 3가지

# 1. 물어보기 -> 주변 지인, 나도코딩 질문게시판 등등

# 2. 디버깅
def std_weight(height, gender): # 키 m 단위 (실수), 성별 '남자' / '여자'
    if gender == '남자':
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = '남성'
weight = round(std_weight(height/100, gender), 2)
print('키 {0}cm {1}의 표준 체중은 {2}kg입니다.'.format(height, gender, weight))
# 상단 메뉴에서 실행 -> 디버깅 시작 or 왼쪽 메뉴에서 벌레 모양 눌러서 '실행 및 디버그'
# create a launch.json.file 클릭 -> 다음부터는 자동으로 python으로 디버깅함
# breakpoint 설정 -> 라인 번호 왼쪽 빨간점 -> 상단 아이콘 중 step over 눌러서 한줄씩 실행
# WATCH(조사식)을 통해 변수나 함수 값을 직접 확인해볼 수 있음
# 실행할 라인을 지나갔으면 원하는 라인 우클릭 -> 커서로 이동
# 라인 16에서 함수를 값이 리턴되어야 하는데 그전에 9번 라인에 breakpoint 넣음으로써 함수 내부로 진입
# gender에 '남자'인지 확인하는데 디버그창에 gender 변수에 '남성'이라는 값이 들어간게 확인됨 -> 고쳐서 문제해결
# call stack 을 통해 실행되는 함수가 어디서 기인한건지 확인가능 -> 문제 해결 실마리

############################################################################################################

# 3. 구글링
# (1). 영어로 검색하라
# (2). 단순하게 검색하라 [사용 언어][핵심 키워드]([OS]) or [사용 언어][에러 메세지]
# 파이썬에서 파일에 쓰는 방법? -> python write file
# 파이썬에서 find와 인덱스 차이? -> python find vs index
# 검색어 뒤에 site:stackoverflow.com 붙이면 stackoverflow 사이트 검색결과만 나옴
# 검색어 뒤에 filetype:pdf 붙이면 pdf형식의 자료만 나옴
# ctrl + 클릭 해서 사이트를 열면 현재창에서 여는것이 아니라 새창에서 열어줌 -> 개꿀팁
# 특정 키워드를 포함하는 페이지 찾기 -> 큰따옴표 사용 -> python "randint vs randrange"
# 특정 키워드를 포함하는 페이지 -> +키워드
# 특정 키워드를 제외하는 페이지 -> -키워드