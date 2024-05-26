# 함수 가변인자

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print(f'이름: {name}\t나이: {age}', end=' ') # end= 구문은 04.py 참고
    print(lang1, lang2, lang3, lang4, lang5)

profile('유재석', 20, 'Python', 'Java', 'C', 'C++', 'C#')
profile('김태호', 25, 'Kotlin', 'Swift', '', '', '')

def profile(name, age, *langauge):
    print(f'이름: {name}\t나이: {age}', end=' ')
    for lang in langauge:
        print(lang, end=' ')
    print() # 줄바꿈 위해 추가

profile('유재석', 20, 'Python', 'Java', 'C', 'C++', 'C#', 'JavaScript')
profile('김태호', 25, 'Kotlin', 'Swift')