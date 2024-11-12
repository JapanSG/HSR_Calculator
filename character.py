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

    def __str__(self) -> str:
        '''String'''
        return (
                f"name : {self.name}\n"
                f"atk : {self._atk}\n"
                f"hp : {self._hp}\n"
                f"spd : {self._spd}"
        )

class Ally(Character):
    '''Ally Class'''
    def __init__(self, name: str, stats: tuple) -> None:
        '''Constructor'''
        super().__init__(name, stats)

class Enemy(Character):
    '''Enemy Class'''
    def __init__(self, name: str, stats: tuple) -> None:
        '''Constructor'''
        super().__init__(name, stats)

if __name__ == "__main__":
    char1 = Character("char1", (100,300,100))
    print(char1)