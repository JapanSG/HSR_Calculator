'''enemy'''
from ally_enemy_base import Enemy
class Baryon(Enemy):
    '''Baryon class'''
    def __init__(self,level, observer, **kwargs):
        '''Constructor'''
        name = "Baryon"
        self.level = level
        atk_data = [12,26,53,98,155,234,338,436,552,663,718]
        hp_data = [45,99,169,293,531,1235,2942,5300,8259,13199,16429]
        hp = self.get_atk_or_hp(hp_data)
        atk = self.get_atk_or_hp(atk_data)
        defe = self.get_base_def()
        spd = self.get_base_spd(83)
        effect_res = self.get_effect_res(0)
        base_stats = (hp,atk,defe,spd)
        super().__init__(name, level, base_stats, observer, effect_res = effect_res, **kwargs)

if __name__ == "__main__":
    baryon = Baryon(80,None)
    print(baryon.stats["hp"])
