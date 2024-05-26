# 모듈
# 모듈은 변수, 함수, 클래스 등의 정의를 담고 있는 .py 파일, import 해서 사용
# 모듈을 사용하면 코드의 가독성을 높이고 유지보수를 용이하게 함

import p28_module
p28_module.price(3) # 3명이서 영화 보러 갔을 때 가격
p28_module.price_moring(4) # 4명이서 조조 영화 보러 갔을 때 가격
p28_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때 가격

import p28_module as mv # 축약
mv.price(3)
mv.price_moring(4)
mv.price_soldier(5)

from p28_module import * # 모든 함수를 import
price(3)
price_moring(4)
price_soldier(5)

from p28_module import price, price_moring # 원하는 함수만 import
price(3)
price_moring(4)
# price_soldier(5) -> 오류 발생

from p28_module import price_soldier as price # 군인만 필요할 때 축약
price(5)