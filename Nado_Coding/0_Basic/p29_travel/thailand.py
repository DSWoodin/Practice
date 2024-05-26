class ThailandPackage:
    def detail(self):
        print('[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원')

# 모듈 내부에서 직접 실행
if __name__ == '__main__':
    print('Thailand 모듈을 직접 실행')
    print('이 문장은 모듈을 직접 실행할 때만 실행되요')
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print('Thailand 외부에서 모듈 호출')

# 매직 메서드 = 스페셜 메서드: 파이썬에서 언더스코어(__)로 시작하고 끝나는 이름 패턴
# __init__은 클래스의 생성자, 초기화를 담당, 객체가 생성되면 자동 호출
# __str__은 객체를 문자열로 표현할 때 호출됨
# __main__은 모듈이 직접 실행될때 해당 모듈이 가진 내용을 정의하는 특별한 모듈 수준 변수
# __main__은 현재 모듈이 최상위 수준에서 실행되는지를 확인하는데 사용됨