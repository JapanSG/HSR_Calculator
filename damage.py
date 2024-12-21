'''damage'''
import random
import custom_exception as ex
from ally_enemy_base import Ally,Enemy
import event

ELEMENTS = ["fire", "ice", "physical", "lightning", "wind", "quantum", "imaginary"]
class Damage:
    '''Damage class'''

    def __init__(self, element : str, mult : float, hits : list, char : Ally, target : Enemy, observer : event.EventManager, **kwargs):
        #ratio between hit ex. (1,1,3) = first hit deals 1/5, second deals 1/5, third deals 3/5
        '''Constructor'''
        self.type = {
            "basic" : kwargs.get('basic', False),
            "skill" : kwargs.get('skill',False),
            "ult" : kwargs.get('ult',False),
            "fua" : kwargs.get('fua',False),
            "dot" : kwargs.get('dot',False),
            "break" : kwargs.get('break',False),
            "additional" : kwargs.get('additional',False)
        }

        self.char = char
        self.target = target
        self.observer = observer

        if element not in ELEMENTS:
            raise ex.NoSuchElement(element)
        self.element = element
        self.mult = mult
        self.hits = hits
        self.base_dmg = round(self.mult * char.total_atk, 2)
        self.dmg_mult = 1 + char.dmg_boost[self.element]
        self.def_mult = 1 - (target.total_def/(target.total_def + 200 + 10 * char.level))
        self.res_mult = 1 - (target.res[self.element] - char.stats["res_pen"])
        self.vulnerability = 1 + target.vulnerable
        self.universal = 1 * (0.9)
        if target.curr_toughness <= 0:
            self.universal = 1

    def __str__(self):
        '''str'''
        return (
            f"Element : {self.element}\n"
            f"Multiplyer : {self.mult}%\n"
            f"Type : {[dtype[0] for dtype in self.type.items() if dtype[1]]}"
        )
    def dmg_formula_ally(self):
        '''Calculate total damage and split the hit'''

        # calculate total damage
        total_dmg = self.base_dmg*self.dmg_mult*self.def_mult*self.res_mult*self.vulnerability*self.universal

        # split the hits in ratio
        dmg_per_hit = [ratio/sum(self.hits)*total_dmg for ratio in self.hits]

        # iterate through each hit in dmg_per hit and calculate if a hit is a critical or not
        for dmg in dmg_per_hit:
            if random.random() <= self.char.stats["crit_rate"]:
                dmg *= 1 + self.char.stats["crit_dmg"]
                event.CritEvent(self.observer).send(self.char, self.target)
                event.DamageEvent(self.observer).send(self.char, self.target, self, dmg)
            else:
                event.DamageEvent(self.observer).send(self.char, self.target, self, dmg)

        # return all hits seperately in a list
        return dmg_per_hit

def __test():
    '''Driver Code'''
    # tingyun = Ally("Tingyun", 50, "lightning", (1086+545, 579+483, 480+113, 112+25),
    #                  crit_rate = 0.088,
    #                  crit_dmg = 0.671,
    #                  break_effect = 0.520,
    #                  lightning_dmg = 0.258
    #                  )
    # silvermane_soldier = Enemy("Silvermane Soldier", 50, (2676.73, 234, 699.3, 83),
    #                              crit_dmg = 0.20,
    #                              effect_res = 0.1,
    #                              physical_res = 0.20,
    #                              fire_res = 0.20,
    #                              ice_res = 0.20,
    #                              lightning_res = 0.20,
    #                              imaginary_res = 0.20
    #                              )
    # dmg = Damage('lightning', 0.6, (3,7), tingyun, silvermane_soldier, basic = True)
    # hits = dmg.dmg_formula_ally()
    # print(dmg.res_mult)
    # print(hits)
    # print(sum(hits))

if __name__ == "__main__":
    __test()
