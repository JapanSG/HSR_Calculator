'''ally'''
from character import Character
import enemy as e
import random
import damage
import skillpoint

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
        self.curr_energy = self.max_energy/2
        self.res_pen = kwargs.get('res_pen', 0.0)
        self.break_efficiency = kwargs.get('break_efficiency', 0.0)
        self.taunt = kwargs.get('taunt', 0.0)

    def __str__(self) -> str:
        '''String'''
        return super().__str__()
    
    def gain_energy(self, num : float) -> None:
        '''Method to gain energy'''
        # min function is to make sure curr_energy is not more than max_energy
        # and max function is for curr_energy to be below 0.
        self.curr_energy = max(min(self.curr_energy + num, self.max_energy),0)

class DestructionTrailblazer(Ally):
    '''DestructionTrailblazer'''
    def __init__(self, level:int,**kwargs) -> None:
        name = "Trailblazer"
        base_stats = (1203,620,460,100)
        super().__init__(name, level, base_stats, **kwargs)

    def __str__(self) -> str:
        '''String'''
        return super().__str__()

    def basic(self, target: e.Enemy, sp : skillpoint.SkillPoint) -> None:
        '''basic attack'''
        sp.use(1)
        dmg_per_hits = damage.Damage('physical', 1, [1], basic = True).dmg_formula_ally(self,target)
        target.curr_hp -= dmg_per_hits[0]

    def skill(self, left_target: e.Enemy, mid_target : e.Enemy, right_target : e.Enemy, sp : skillpoint.SkillPoint) -> None:
        '''skill'''
        if sp.curr:
            sp.use(-1)
            dmg_per_hits_left = damage.Damage('physical', 1.25, [1], skill = True).dmg_formula_ally(self,left_target)
            left_target.curr_hp -= dmg_per_hits_left[0]
            dmg_per_hits_mid = damage.Damage('physical', 1.25, [1], skill = True).dmg_formula_ally(self,mid_target)
            mid_target.curr_hp -= dmg_per_hits_mid[0]
            dmg_per_hits_right = damage.Damage('physical', 1.25, [1], skill = True).dmg_formula_ally(self,right_target)
            right_target.curr_hp -= dmg_per_hits_right[0]



    def ultimate(self, target: e.Enemy) -> None:
        '''ultimate'''


if __name__ == "__main__":
    sp = skillpoint.SkillPoint()
    mc = DestructionTrailblazer(80, taunt = 125.0)
    enemy = e.Enemy("enemy",80,(2000,500,500,80))
