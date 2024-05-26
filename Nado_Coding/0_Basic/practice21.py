# 마린 : 공격 유닛, 군인, 총을 쏨
name = '마린' # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력
print('{0} 유닛이 생성되었습니다.'.format(name))
print('체력 {0}, 공격력 {1}\n'.format(hp,damage))

# 탱크: 공격 유닛, 탱크, 포를 쏨. 일반 모드 / 시즈 모드
tank_name = '탱크'
tank_hp = 150
tank_damage = 35

print('{0} 유닛이 생성되었습니다.'.format(tank_name))
print('체력 {0}, 공격력 {1}\n'.format(tank_hp, tank_damage))

def attack(name, location, damage):
    print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format( \
        name, location, damage))
    
attack(name, '1시', damage)
attack(tank_name, '1시', tank_damage)

########################################################################################

# 클래스와 멤버변수

class Unit:
    def __init__(self, name, hp, damage): # 메서드 앞에는 항상 self를 붙임. 자기 자신을 의미
        #__init__은 객체의 초기화를 담당하는 메서드, 객체가 생성될 때 자동으로 호출됨
        self.name = name # name, hp, damage는 Unit class의 멤버변수임
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}\n'.format(self.hp, self.damage))

marine1 = Unit('마린', 40, 5) # marine1,2,tank처럼 class로 부터 만들어진 것을 객체라고 함
marine2 = Unit('마린', 40, 5) # marine1,2,tank는 Unit class의 인스턴스라고 표현함
tank = Unit('탱크', 150, 35) # self를 제외하고, name, hp, damage 3개의 값은 넣어줘야 함

# 레이스: 공중 유닛, 비행기, 클로킹(상대에게 보이지 않음)
wraith1 = Unit('레이스', 80, 5)
print('유닛 이름: {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage))
# .name, .damage 등을 사용해 class 외부에서도 멤버변수를 호출할 수 있음

# 마인드 컨트롤: 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit('빼앗은 레이스', 80, 5)
wraith2.clocking = True # .clocking은 Unit class에서 만들었던 멤버변수가 아님
if wraith2.clocking == True: # 하지만 class 외부에서도 새로운 멤버변수를 만들어 줄수 있음
    print('{0} 는 현재 클로킹 상태입니다.'.format(wraith2.name))
# 확장된 멤버변수는 확장한 객체에서만 사용할 수 있음 --> wraith1.clocking은 불가함