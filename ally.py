'''ally'''
from character import Character
import enemy as e
import random
import skillpoint
import setting

class Ally(Character):
    '''Ally Class'''
    def __init__(self, name: str, level: int, base_stats: tuple, **kwargs) -> None:
        '''Constructor
            hidden_stats =  (
                            res_pen : float
                            break_efficiency: float,
                            taunt: float
                            )
        '''
        super().__init__(name, level, base_stats, **kwargs)
        self.res_pen = kwargs.get('res_pen', 0.0)
        self.break_efficiency = kwargs.get('break_efficiency', 0.0)
        self.taunt = kwargs.get('taunt', 0.0)

    def __str__(self) -> str:
        '''String'''
        return super().__str__()

class DestructionTrailblazer(Ally):
    '''DestructionTrailblazer'''
    def __init__(self,**kwargs) -> None:
        name = "Trailblazer"
        base_stats = (1203,620,460,100)
        super().__init__(name, base_stats, **kwargs)

    def __str__(self) -> str:
        '''String'''
        return super().__str__()

    def basic(self, target: e.Enemy) -> None:
        '''basic attack'''
        setting.SP.use(1)

    def skill(self, target: e.Enemy) -> None:
        '''skill'''


    def ultimate(self, target: e.Enemy) -> None:
        '''ultimate'''


if __name__ == "__main__":
    mc = DestructionTrailblazer(taunt = 125.0)
    print(mc.dmg_boost['physical'])
