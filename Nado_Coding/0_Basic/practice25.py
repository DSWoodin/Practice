# super() 구문

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name 
        self.hp = hp
        self.speed = speed
    
class BuildingUnit(Unit): # 건물
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0) 
        super().__init__(name, hp, 0) # 건물은 이동을 못하므로 speed에 0
        self.location = location
        # 라인 11, 라인 12는 같은 문장임
        # super()를 쓸때는 self를 쓰지 않아도 됨

class Mob:
    def __init__(self):
        print('Mob 생성자')

class Flyable:
    def __init__(self):
        print('Flyable 생성자')

class FlyableMob(Mob, Flyable):
    def __init__(self):
        # super().__init__()
        # 다중상속받은 클래스 내에서 super() 구문을 사용하면 맨 처음 상속받은 클래스만 호출됨
        # 따라서 다중상속받은 경우에는 클래스를 따로 따로 호출해야
        Mob.__init__(self)
        Flyable.__init__(self)

dropship = FlyableMob() # 드랍쉽

###########################################################################################

# pass

# pass는 문법적으로 실행문이 필요한 상황에서 아무 동작도 시키지 않을때 사용
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass 

# 서플라이 디폿: 건물(유닛 저장소), 1개 건물 최대 8 유닛
supply_depot = BuildingUnit('서플라이 디폿', 500, '7시')

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    pass

game_start()
game_over()