# pip install을 통한 패키지 설치

# 파이썬에는 누군가가 만든, 만들고 있는 수많은 패키지가 존재함
# 새로운 코드를 작성하는 능력도 중요하지만
# 기존에 잘 만들어진 패키지를 필요한 곳에 잘 가져다가 쓰는 것도 매우 중요함

# 구글에 pypi 검색 -> https://pypi.org/
# 웹 스크레이핑 패키지로 유명한 beautifulsoup 검색
# 터미널에 pip install beautifulsoup4
# 예제를 긁어와서 실행

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 현재 설치되어 있는 패키지 목록 확인 -> pip list
# 패키지 정보 확인 -> pip show beautifulsoup4
# 패키지 업데이트 -> pip install --upgrade beautifulsoup4
# 패키지 삭제 -> pip uninstall beautifulsoup4

# 라이브러리와 패키지는 약간 다른 개념
# 라이브러리는 코드의 모음, 패키지는 모듈을 관리하기 위한 방법 중 하나
# 하나의 라이브러리에는 여러 개의 패키지가 포함될 수 있음
# 패키지 안에는 여러 개의 모듈이 있을 수 있음