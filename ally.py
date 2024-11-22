'''ally'''
from character import Character
import enemy as e
import random
import skillpoint
import setting

class Ally(Character):
    '''Ally Class'''
    def __init__(self, name: str, base_stats: tuple, **kwargs) -> None:
        '''Constructor
            hidden_stats =  (
                            break_efficiency: float,
                            taunt: float
                            )
        '''
        super().__init__(name, base_stats, **kwargs)
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
        base_dmg = self.atk
        dmg_boost_mult = 1 + self.physical_dmg
        def_mult = 1 - (target.defe/(target.defe+200+10*80))
        res_mult = 1 - (target.physical_res)
        dmg_taken_mult = 1
        universal_mult = 1*(0.9)
        crit_mult = 1
        if random.random() <= self.crit_rate:
            crit_mult += self.crit_dmg
        dmg = base_dmg*def_mult*dmg_boost_mult*res_mult*dmg_taken_mult*universal_mult*crit_mult
        target.hp -= dmg

    def skill(self, target: e.Enemy) -> None:
        '''skill'''


    def ultimate(self, target: e.Enemy) -> None:
        '''ultimate'''


if __name__ == "__main__":
    mc = DestructionTrailblazer(taunt = 125.0)
    print(mc)
