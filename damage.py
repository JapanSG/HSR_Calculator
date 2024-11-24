'''damage'''
import custom_exception as ex
import random
import ally as a
import enemy as e
ELEMENTS = ["fire", "ice", "physical", "lightning", "wind", "quantum", "imaginary"]
class Damage:
    '''Damage class'''

    def __init__(self, element : str, mult : float, hits : list, **kwargs):
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
        
        if element not in ELEMENTS:
            raise ex.NoSuchElement(element)
        self.element = element
        self.mult = mult
        self.hits = hits

    def __str__(self):
        '''str'''
        return (
            f"Element : {self.element}\n"
            f"Multiplyer : {self.mult}%\n"
            f"Type : {[dtype[0] for dtype in self.type.items() if dtype[1]]}"
        )
    def dmg_formula_ally(self, char: a.Ally, target: e.Enemy):
        '''Calculate total damage and split the hit'''
        #calculate damage before crits
        base_dmg = round(self.mult * char.atk,2)
        dmg_mult = 1 + char.dmg_boost[self.element]
        def_mult = 1 - (target.defe/(target.defe + 200 + 10 * char.level))
        res_mult = 1 - (target.res[self.element] - char.res_pen)
        vulnerability = 1 + target.vulnerable
        universal = 1*(0.9)
        if target.curr_toughness <= 0:
            universal = 1
        # calculate total damage
        total_dmg = base_dmg*dmg_mult*def_mult*res_mult*vulnerability*universal

        # split the hits in ratio
        dmg_per_hit = [ratio/sum(self.hits)*total_dmg for ratio in self.hits]

        # iterate through each hit in dmg_per hit and calculate if a hit is a critical or not 
        for i in range(len(dmg_per_hit)):
            if random.random() <= char.crit_rate:
                dmg_per_hit[i] *= 1 + char.crit_dmg

        # return all hits seperately in a list
        return dmg_per_hit

def __test():
    '''Driver Code'''
    tingyun = a.Ally("Tingyun", 50, (1086+545, 579+483, 480+113, 112+25),
                     crit_rate = 0.088,
                     crit_dmg = 0.671,
                     break_effect = 0.520,
                     lightning_dmg = 0.258
                     )
    silvermane_soldier = e.Enemy("Silvermane Soldier", 50, (2676.73, 234, 699.3, 83),
                                 crit_dmg = 0.20,
                                 effect_res = 0.1,
                                 physical_res = 0.20,
                                 fire_res = 0.20,
                                 ice_res = 0.20,
                                 lightning_res = 0.20,
                                 imaginary_res = 0.20
                                 )
    dmg = Damage('lightning', 0.6, (3,7), basic = True)
    hits = dmg.dmg_formula_ally(tingyun,silvermane_soldier)
    print(hits)
    print(sum(hits))

if __name__ == "__main__":
    __test()
