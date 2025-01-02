'''character'''
from character import Character
import relic as r
import event
class Ally(Character):
    '''Ally Class'''
    def __init__(self, name: str, level: int, element : str, base_stats: tuple, observer : event.EventManager, **kwargs) -> None:
        '''Constructor
            hidden_stats =  (
                            res_pen : float
                            break_efficiency: float,
                            taunt: float
                            )
        '''
        super().__init__(name, level, base_stats, observer, **kwargs)
        self.element = element
        self.stats["res_pen"] = kwargs.get('res_pen', 0.0)
        self.stats["break_efficiency"] = kwargs.get('break_efficiency', 0.0)
        self.stats["taunt"] = kwargs.get('taunt', 0.0)

        self.curr_energy = self.stats["max_energy"]/2

        self.relics = {
            "head"      : None,
            "hands"     : None,
            "body"      : None,
            "feet"      : None,
            "rope"       : None,
            "sphere"    : None
        }

    def gain_energy(self, num : float) -> None:
        '''Method to gaining energy'''
        # min function is to make sure curr_energy is not more than max_energy
        # and max function is for curr_energy to not be below 0.
        self.curr_energy = max(min(self.curr_energy + num*(1 + self.stats["energy_regen_rate"]), self.stats["max_energy"]),0)

    def use_energy(self, num : float) -> None:
        '''Method for using energy'''
        self.curr_energy -= num

    def equip(self, *relics) -> None:
        '''Equip Relic'''
        for relic in relics:
            if isinstance(relic, r.Head):
                self.relics["head"] = relic
                self.stats[relic.main_stat.stat] += relic.main_stat.num
            elif isinstance(relic, r.Hands):
                self.relics["hands"] = relic
                self.stats[relic.main_stat.stat] += relic.main_stat.num
            elif isinstance(relic, r.Body):
                self.relics["body"] = relic
                self.stats[relic.main_stat.stat] += relic.main_stat.num
            elif isinstance(relic, r.Feet):
                self.relics["feet"] = relic
                self.stats[relic.main_stat.stat] += relic.main_stat.num
            elif isinstance(relic, r.Rope):
                self.relics["rope"] = relic
                self.stats[relic.main_stat.stat] += relic.main_stat.num
            elif isinstance(relic, r.Sphere):
                self.relics["sphere"] = relic
                self.stats[relic.main_stat.stat] += relic.main_stat.num
            else:
                raise ValueError
        self.check_relic_passive()

    def check_relic_passive(self) -> None:
        '''Check if relic can activate'''
        keys = self.relics.keys()
        memo = []
        for key1 in keys:
            count = 0
            setid = self.relics[key1].setid
            if setid in memo:
                continue
            memo.append(setid)
            for key2 in keys:
                if self.relics[key2].setid == setid:
                    count += 1
            if count >= 2:
                event.Relic2pcPassive(self.observer).send(self, self.relics[key1])
            if count >= 4:
                event.Relic4pcPassive(self.observer).send(self, self.relics[key1])

    def update(self,lis : list):
        '''update event'''
        #got hit
        if lis[0] == event.DamageEvent and lis[2] is self:
            self.curr_hp -= lis[3]
            self.gain_energy(5)

        #activate 2pc relics
        elif lis[0] == event.Relic2pcPassive and lis[1] is self:
            lis[2].passive_2pc(self)

        #activate 4pc relics
        elif lis[0] == event.Relic4pcPassive and lis[1] is self:
            lis[2].passive_4pc(self, self.observer)

class Enemy(Character):
    '''Enemy Class'''

    def __init__(self, name: str, level:int, base_stats : tuple, observer : event.EventManager, **kwargs) -> None:
        '''Constructor'''
        super().__init__(name, level, base_stats, observer, **kwargs)
        self.stats["crit_rate"] = 0

        self.toughness = kwargs.get('toughness', 30)
        self.curr_toughness = self.toughness

    def get_base_def(self):
        '''return base def base on level'''
        base_def = 200 + 10 * self.level
        return base_def

    def get_base_spd(self, spd):
        '''return base spd base on level'''
        level = self.level
        if level < 65:
            spd *= 1
        elif level < 78:
            spd *= 1.1
        elif level < 86:
            spd *= 1.2
        else:
            spd *= 1.32
        return spd
    #FIXME : hp scaling currently is linear using linear interpolation fix this by changing it to quardratic scaling
    def get_atk_or_hp(self, lis):
        '''get base atk and hp'''
        lvb = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
        lvb = list(zip(lvb, lis))
        if 0 > self.level > 95:
            raise ValueError(f"Invalid level '{self.level}'")
        q, r = divmod(self.level, 10)
        length = len(lvb)
        for i in range(length):
            if lvb[i][0]//10 == q:
                stats_per_level = (lvb[i+1][1] - lvb[i][1]) / (lvb[i+1][0] - lvb[i][0])
                return stats_per_level*r + lvb[i][1]
        return -1

    def get_effect_res(self, effect_res):
        '''return effect_res base on level'''
        additional = 0.004 * min(max(0, self.level-50), 25)
        effect_res += additional
        return effect_res

    def update(self, lis):
        '''update event'''
        ##get hit
        if lis[0] == event.DamageEvent and lis[2] is self:
            self.curr_hp -= lis[4]


if __name__ == "__main__":
    a = Enemy("test", 93, (0,0,0,0), None)
    data = [12,26,53,98,155,234,338,436,552,663,718]
    atk = a.get_atk_or_hp(data)
    print(a.level)
    print(atk)
