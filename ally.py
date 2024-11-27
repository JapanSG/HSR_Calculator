'''ally'''
from character import Ally
import enemy as e
import random
import damage
import skillpoint

class DestructionTrailblazer(Ally):
    '''DestructionTrailblazer'''
    def __init__(self, level:int,**kwargs) -> None:
        name = "Trailblazer"
        base_stats = (1203,620,460,100)
        super().__init__(name, level, base_stats, max_energy =  120, **kwargs)

    def __str__(self) -> str:
        '''String'''
        return super().__str__()

    def basic(self, target: e.Enemy, sp : skillpoint.SkillPoint) -> None:
        '''basic attack'''
        sp.use(1)
        dmg_per_hits = damage.Damage('physical', 1, [1], basic = True).dmg_formula_ally(self,target)
        target.curr_hp -= dmg_per_hits[0]
        self.gain_energy(20)

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
        self.gain_energy(30)


    def ultimate(self, left_target: e.Enemy, mid_target : e.Enemy, right_target : e.Enemy) -> None:
        '''ultimate'''
        self.use_energy(self.max_energy)
        choose = input("Choose mode (1 = single, 2 = double) -> ")
        if choose == "1":
            dmg_per_hits = damage.Damage('physical', 4.5, [1], basic = True).dmg_formula_ally(self,mid_target)
            mid_target.curr_hp -= dmg_per_hits[0]
        else:
            dmg_per_hits_left = damage.Damage('physical', 1.62, [1], skill = True).dmg_formula_ally(self,left_target)
            left_target.curr_hp -= dmg_per_hits_left[0]
            dmg_per_hits_mid = damage.Damage('physical', 2.7, [1], skill = True).dmg_formula_ally(self,mid_target)
            mid_target.curr_hp -= dmg_per_hits_mid[0]
            dmg_per_hits_right = damage.Damage('physical', 1.62, [1], skill = True).dmg_formula_ally(self,right_target)
            right_target.curr_hp -= dmg_per_hits_right[0]
        self.gain_energy(5)

if __name__ == "__main__":
    sp = skillpoint.SkillPoint()
    mc = DestructionTrailblazer(80, taunt = 125.0)
    enemy = e.Enemy("enemy",80,(2000,500,500,80))
