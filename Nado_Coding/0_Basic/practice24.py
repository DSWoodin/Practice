# 메서드 오버라이딩

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name 
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]' \
            .format(self.name, location, self.speed))

class AttackUnit(Unit): 
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed)
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

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0}: {1} 방향으로 날아갑니다. [속도 {2}]' \
            .format(name, location, self.flying_speed))
        
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) 
        # 여기서 0에 해당하는 부분은 지상 유닛의 speed임
        # 공중 유닛의 speed는 flying_speed에 들어가므로 지상 speed는 0으로 처리
        Flyable.__init__(self, flying_speed)

    def move(self, location): # Unit class에서 정의했던 move 함수를 재정의
        print('[공중 유닛 이동]') 
        self.fly(self.name, location)
        # 메서드 오버라이딩
    
# 벌쳐: 지상 유닛, 기동성이 좋음
vulture = AttackUnit('벌쳐', 80, 10, 20)

# 배틀크루져: 공중 유닛, 체력 높음. 공격력 높음
battlecruiser = FlyableAttackUnit('배틀크루져', 500, 25, 3)

vulture.move('11시')
battlecruiser.fly(battlecruiser.name, '9시')
# battlecruiser.name 은 새로운 멤버변수를 만든 것임
# 지상유닛은 move를 써야하고 공중유닛은 fly를 사용해야 하는 상황
# 매번 그 유닛이 지상인지 공중인지 확인해야하는 번거로움 발생
# 메서드 오버라이딩을 통해서 편하게 처리 --> 라인 45~47

battlecruiser.move('9시')
# 배틀크루져를 FlyableAttackUnit class로 만들었으므로 재정의된 move 함수를 따름

vulture.move('11시')
# 벌쳐는 AttackUnit(Unit) class로 만들었으므로 원래 Unit 에서 정의된 move 함수를 따름