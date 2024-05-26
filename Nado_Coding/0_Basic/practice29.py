# 패키지 -> 모듈을 모아놓은 집합

import p29_travel.thailand # 패키지나 모듈은 import 뒤에 py 제외하고 입력
trip_to = p29_travel.thailand.ThailandPackage()
trip_to.detail()

# 클래스를 바로 import 하면 오류 발생
# import p29_travel.thailand.ThailandPackage -> 오류 발생
# from import 구문을 사용하면 가능
from p29_travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from p29_travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# # __all__ -> __init__.py 참조
from p29_travel import *
trip_to1 = vietnam.VietnamPackage()
trip_to2 = thailand.ThailandPackage()
trip_to1.detail()
trip_to2.detail()

# 패키지, 모듈의 위치 확인
import inspect
import random 
print(inspect.getfile(random))
print(inspect.getfile(thailand))
# random 처럼 기본 내장 패키지가 들어있는 경로를 확인해서
# 본인이 만든 패키지를 해당 경로에 저장하여 보관해도 잘 동작함
# 패키지 유지관리를 용이하게 하여 이 패키지를 다른 프로젝트에도 사용할 수 있음 