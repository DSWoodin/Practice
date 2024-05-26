# 메서드

class AttackUnit:
    def __init__(self, name, hp, damage): 
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]' \
            .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))
    
# 파이어뱃: 공격 유닛, 화염방사기
firebat1 = AttackUnit('파이어뱃', 50, 16)
firebat1.attack('5시')
firebat1.damaged(25)
firebat1.damaged(25) # 공격 2번 받는다고 가정

# 함수와 메서드는 비슷하지만 약간 다른 개념
# 함수는 독립적으로 존재하는 코드 블럭, 메서드는 클래스나 객체에 속한 함수
# 메서드는 클래스 내에 정의 되어 있고, 첫 번째 매개변수로 self를 가짐