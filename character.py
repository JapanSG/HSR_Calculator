'''character'''
class Character:
    '''Character class'''
    def __init__(self, name :str, level:int, base_stats : tuple, **kwargs) -> None:
        '''
        Constructor
        name = character name : str
        level = (1 to 80)
        base_stats =        (
                            hp:float,
                            atk:float,
                            defe:float,
                            spd:float
                            )

        **kwargs
        advanced_stats =    (
                            crit_rate: float,
                            crit_dmg: float,
                            break_effect: float,
                            outgoing_healing: float,
                            max_energy: float,
                            energy_regen_rate: float,
                            effect_hit_rate: float,
                            effect_res: float
                            )

        dmg_boost =         (
                            physical_dmg: float,
                            fire_dmg: float,
                            ice_dmg: float,
                            lightning_dmg: float,
                            wind_dmg: float,
                            quantum_dmg: float,
                            imaginary_dmg: float
                            )

        dmg_res =           (
                            physical_res:float,
                            fire_res: float,
                            ice_res: float,
                            lightning_res: float,
                            wind_res: float,
                            quantum_res: float,
                            imaginary_res: float
                            )

        other_stats =      (
                            vulnerable : float,
                            curr_hp: float,
                            break_efficiency: float,
                            taunt: float
                            )
        '''
        self.name = name
        self.level = level
        self.hp, self.atk, self.defe, self.spd = base_stats
        self.curr_hp = self.hp

        self.crit_rate = kwargs.get('crit_rate', 0.05)
        self.crit_dmg = kwargs.get('crit_dmg', 0.50)
        self.break_effect = kwargs.get('break_effect', 0.0)
        self.outgoing_healing = kwargs.get('outgoing_healing', 0.0)
        self.max_energy = kwargs.get('max_energy', 0.0)
        self.energy_regen_rate = kwargs.get('energy_regen_rate', 0.0)
        self.effect_hit_rate = kwargs.get('effect_hit_rate', 0.0)
        self.effect_res = kwargs.get('effect_res', 0.0)

        self.dmg_boost = {
            'physical' : kwargs.get('physical_dmg', 0.0),
            'fire' : kwargs.get('fire_dmg', 0.0),
            'ice' : kwargs.get('ice_dmg', 0.0),
            'lightning' : kwargs.get('lightning_dmg', 0.0),
            'wind' : kwargs.get('wind_dmg', 0.0),
            'quantum' : kwargs.get('quantum_dmg', 0.0),
            'imaginary' : kwargs.get('imaginary_dmg', 0.0)
        }

        self.res = {
            'physical' : kwargs.get('physical_res', 0.0),
            'fire' : kwargs.get('fire_res', 0.0),
            'ice' : kwargs.get('ice_res', 0.0),
            'lightning' : kwargs.get('lightning_res', 0.0),
            'wind' : kwargs.get('wind_res', 0.0),
            'quantum' : kwargs.get('quantum_res', 0.0),
            'imaginary' : kwargs.get('imaginary_res', 0.0)
        }

        self.vulnerable = kwargs.get('vulnerable', 0.0)

    def __str__(self) -> str:
        '''String'''
        return f"{self.name}"

    def __repr__(self) -> str:
        '''repr'''
        return self.__str__()

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
        '''Method to gaining energy'''
        # min function is to make sure curr_energy is not more than max_energy
        # and max function is for curr_energy to not be below 0.
        self.curr_energy = max(min(self.curr_energy + num*(1 + self.energy_regen_rate), self.max_energy),0)

    def use_energy(self, num : float) -> None:
        '''Method for using energy'''
        self.curr_energy -= num

class Enemy(Character):
    '''Enemy Class'''
    def __init__(self, name: str, level:int, base_stats : tuple, **kwargs) -> None:
        '''Constructor'''
        super().__init__(name, level, base_stats, **kwargs)
        self.crit_rate = 0
        self.toughness = kwargs.get('toughness', 30)
        self.curr_toughness = self.toughness

    def __str__(self):
        '''String'''
        return super().__str__()

if __name__ == "__main__":
    pass