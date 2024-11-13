'''character'''
class Character:
    '''Character class'''
    def __init__(self, name :str, stats : tuple) -> None:
        '''
        Constructor
        stats = (atk:float, hp:float, spd:float)
        '''
        self.name = name
        self._atk, self._hp, self._spd = stats

    def __str__(self) -> str:
        '''String'''
        stats = self.get_atk(),self.get_hp(),self.get_spd()
        return f"{self.name}{stats}"

    def __repr__(self) -> str:
        '''repr'''
        return self.__str__()

    def set_atk(self, atk : float) -> None:
        '''Set atk'''
        self._atk = atk

    def get_atk(self) -> float:
        '''Get atk'''
        return self._atk

    def set_hp(self, hp : float) -> None:
        '''Set hp'''
        self._hp = hp

    def get_hp(self) -> float:
        '''Get hp'''
        return self._hp

    def set_spd(self, spd : float) -> None:
        '''Set spd'''
        self._spd = spd

    def get_spd(self) -> float:
        '''Get spd'''
        return self._spd


class Enemy(Character):
    '''Enemy Class'''
    def __init__(self, name: str, stats: tuple) -> None:
        '''Constructor'''
        super().__init__(name, stats)

    def __str__(self):
        '''String'''
        return super().__str__()

class Ally(Character):
    '''Ally Class'''
    def __init__(self, name: str, stats: tuple) -> None:
        '''Constructor'''
        super().__init__(name, stats)

    def __str__(self) -> str:
        '''String'''
        return super().__str__()

    def basic(self, enemy : Enemy):
        '''attack a enemy'''
        enemy_hp = enemy.get_hp()
        new_hp = enemy_hp - self.get_atk()
        if new_hp < 0 :
            new_hp = 0
        enemy.set_hp(new_hp)

if __name__ == "__main__":
    char1 = Character("char1", (100,300,100))
    char2 = Ally("char2", (100,300,100))
    print([char1,char2])