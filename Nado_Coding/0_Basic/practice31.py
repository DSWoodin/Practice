# 내장함수: 파이썬 언어 자체에 내장되어 import 없이 사용가능한 함수
# int(), round(), open(), range(), print(), input(), try:, ...
# 구글링 list of python builtins 내장 함수의 목록을 확인 가능

# dir() : 해당 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random
print(dir()) # random이 추가된 모습
print(dir(random))
lst = [1, 2, 3]
print(dir(lst))
name = 'Jim'
print(dir(name))

# 외장함수: 파이썬 표준 라이브러리 혹은 서드파티 라이브러리
          # (다른 개발자가 만든 라이브러리)에 포함되어 있어
          # import를 통해 해당 모듈을 임포트해야 사용가능한 함수
# 구글링 list of python modules 외장 함수의 목록을 확인 가능

# glob: 경로 내의 폴더 / 파일 목록 조회 (= 윈도우 dir -> 28번 라인)
import glob
print(glob.glob('*.py'))
print(glob.glob('/pythonworkspace/Nado Coding/*.py')) # 확장자가 py 인 모든 파일

# os: 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리
print(os.listdir()) # glob과 비슷함

folder = 'p31_sample_dir'
if os.path.exists(folder):
    print('이미 존재하는 폴더입니다.')
    os.rmdir(folder) # 폴더를 삭제하는 함수
    print(folder, '폴더를 삭제하였습니다.')
else:
    os.makedirs(folder) # 폴더를 생성하는 함수
    print(folder, '폴더를 생성하였습니다.')

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
print('오늘 날짜는 ', datetime.date.today())
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
# timedelta : 두 날짜 사이의 간격
print('우리가 만난지 100일은', today + td) # 오늘부터 100일 후