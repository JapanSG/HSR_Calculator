'''character'''
class Character:
    '''Character class'''
    def __init__(self, name :str, base_stats : tuple, **kwargs) -> None:
        '''
        Constructor
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
                            curr_hp: float,
                            break_efficiency: float,
                            taunt: float
                            )
        '''
        self.name = name
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

        self.physical_dmg = kwargs.get('physical_dmg', 0.0)
        self.fire_dmg = kwargs.get('fire_dmg', 0.0)
        self.ice_dmg = kwargs.get('ice_dmg', 0.0)
        self.lightning_dmg = kwargs.get('lightning_dmg', 0.0)
        self.wind_dmg = kwargs.get('wind_dmg', 0.0)
        self.quantum_dmg = kwargs.get('quantum_dmg', 0.0)
        self.imaginary_dmg = kwargs.get('imaginary_dmg', 0.0)

        self.physical_res = kwargs.get('physical_res', 0.0)
        self.fire_res = kwargs.get('fire_res', 0.0)
        self.ice_res = kwargs.get('ice_res', 0.0)
        self.lightning_res = kwargs.get('lightning_res', 0.0)
        self.wind_res = kwargs.get('wind_res', 0.0)
        self.quantum_res = kwargs.get('quantum_res', 0.0)
        self.imaginary_res = kwargs.get('imaginary_res', 0.0)

    def __str__(self) -> str:
        '''String'''
        return f"{self.name}"

    def __repr__(self) -> str:
        '''repr'''
        return self.__str__()

if __name__ == "__main__":
    pass