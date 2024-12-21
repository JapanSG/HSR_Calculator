"""character"""

from character import Character
import relic as r
import event


class Ally(Character):
    """Ally Class"""

    def __init__(
        self,
        name: str,
        level: int,
        element: str,
        base_stats: tuple,
        observer: event.EventManager,
        **kwargs
    ) -> None:
        """Constructor
        hidden_stats =  (
                        res_pen : float
                        break_efficiency: float,
                        taunt: float
                        )
        """
        super().__init__(name, level, base_stats, observer, **kwargs)
        self.element = element
        self.stats["res_pen"] = kwargs.get("res_pen", 0.0)
        self.stats["break_efficiency"] = kwargs.get("break_efficiency", 0.0)
        self.stats["taunt"] = kwargs.get("taunt", 0.0)

        self.curr_energy = self.stats["max_energy"] / 2

        self.relics = {
            "head": None,
            "hands": None,
            "body": None,
            "feet": None,
            "rope": None,
            "sphere": None,
        }

    def gain_energy(self, num: float) -> None:
        """Method to gaining energy"""
        # min function is to make sure curr_energy is not more than max_energy
        # and max function is for curr_energy to not be below 0.
        self.curr_energy = max(
            min(
                self.curr_energy + num * (1 + self.stats["energy_regen_rate"]),
                self.stats["max_energy"],
            ),
            0,
        )

    def use_energy(self, num: float) -> None:
        """Method for using energy"""
        self.curr_energy -= num

    def equip(self, *relics) -> None:
        """Equip Relic"""
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
        """Check if relic can activate"""
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

    def update(self, lis: list):
        """update event"""
        if lis[0] == event.DamageEvent and lis[2] is self:
            self.curr_hp -= lis[3]
            self.gain_energy(5)
        elif lis[0] == event.Relic2pcPassive and lis[1] is self:
            lis[2].passive_2pc(self)
        elif lis[0] == event.Relic4pcPassive and lis[1] is self:
            lis[2].passive_4pc(self, self.observer)


class Enemy(Character):
    """Enemy Class"""

    def __init__(
        self,
        name: str,
        level: int,
        base_stats: tuple,
        observer: event.EventManager,
        **kwargs
    ) -> None:
        """Constructor"""
        super().__init__(name, level, base_stats, observer, **kwargs)
        self.stats["crit_rate"] = 0

        self.toughness = kwargs.get("toughness", 30)
        self.curr_toughness = self.toughness

    def __str__(self):
        """String"""
        return super().__str__()

    def update(self, lis):
        """update event"""
        ##get hit
        if lis[0] == event.DamageEvent and lis[2] is self:
            self.curr_hp -= lis[4]


if __name__ == "__main__":
    pass
