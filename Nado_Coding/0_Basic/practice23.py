# 상속

class Unit:
    def __init__(self, name, hp):
        self.name = name 
        self.hp = hp
# 메딕: 의무병, 데미지 없음

class AttackUnit:
    def __init__(self, name, hp, damage): 
        self.name = name
        self.hp = hp
        self.damage = damage
# Unit과 AttackUnit 클래스에서 겹치는 부분이 있음

# 겹치는 부분을 AtttackUnit으로 상속하기
class AttackUnit(Unit): # 여기서 Unit을 부모class, AttackUnit을 자식class라고 표현
    def __init__(self, name, hp, damage): 
        Unit.__init__(self, name, hp)
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

firebat1 = AttackUnit('파이어뱃', 50, 16)
firebat1.attack('5시')
firebat1.damaged(25)
firebat1.damaged(25)

# 드랍쉽: 공중 유닛, 수송기, 마린, 파이어뱃, 탱크 등을 수송, 공격 X
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0}: {1} 방향으로 날아갑니다. [속도 {2}]' \
            .format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속은 콤마(,)를 사용
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
valkyrie.fly(valkyrie.name, '3시') # valkyrie.name은 새로운 멤버변수를 만든 것임