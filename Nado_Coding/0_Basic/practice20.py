# pickle

import pickle
profile_file = open('practice20.profile.pickle', 'wb') 
# 'wb'에서 w는 write(쓰기 모드), b는 binary 타입을 의미, 피클은 인코딩 설정 필요없음
profile = {'이름':'박명수', '나이':30, '취미':['축구', '골프', '코딩']}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
profile_file.close()

import pickle
profile_file = open('practice20.profile.pickle', 'rb') # 읽기 모드
profile = pickle.load(profile_file) # profile_file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

# with 구문

import pickle
with open('practice20.profile.pickle', 'rb') as profile_file: 
    # 읽기 모드로 열고 profile_file에 저장
    print(pickle.load(profile_file)) # with 문 사용하면 close 할 필요 없음

with open('practice20.txt', 'w', encoding='utf8') as study_file:
    study_file.write('파이썬을 열심히 공부하고 있어요')

with open('practice20.txt', 'r', encoding='utf8') as study_file:
    print(study_file.read())