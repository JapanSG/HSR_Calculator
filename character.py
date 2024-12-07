'''character_base_class'''
import event
class Character:
    '''Character class'''
    def __init__(self, name :str, level:int, base_stats : tuple, observer : event.EventManager, **kwargs) -> None:
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

        self.stats = {
            "hp"                : base_stats[0],
            "hp_per"            : kwargs.get('hp_per', 0.0),
            "hp_flat"           : kwargs.get('hp_flat', 0.0),

            "atk"               : base_stats[1],
            "atk_per"           : kwargs.get("atk_per", 0.0),
            "atk_flat"          : kwargs.get("atk_flat", 0.0),

            "defe"              : base_stats[2],
            "def_per"           : kwargs.get("def_per", 0.0),
            "def_flat"          : kwargs.get("def_flat", 0.0),

            "spd"               : base_stats[3],
            "spd_per"           : kwargs.get("spd_per", 0.0),
            "spd_flat"          : kwargs.get("spd_flat", 0.0),

            "crit_rate"         : kwargs.get('crit_rate', 0.05),
            "crit_dmg"          : kwargs.get('crit_dmg', 0.50),
            "break_effect"      : kwargs.get('break_effect', 0.0),
            "outgoing_healing"  : kwargs.get('outgoing_healing', 0.0),
            "max_energy"        : kwargs.get('max_energy', 0.0),
            "energy_regen_rate" : kwargs.get('energy_regen_rate', 0.0),
            "effect_hit_rate"   : kwargs.get('effect_hit_rate', 0.0),
            "effect_res"        : kwargs.get('effect_res', 0.0),

            "def_reduction"     : kwargs.get('def_reduction', 0.0),
            "def_ignore"        : kwargs.get('def_ignore', 0.0)
        }

        self.name = name
        self.level = level

        self.total_hp = self.stats["hp"] * (1 + self.stats["hp_per"]) + self.stats["hp_flat"]
        self.curr_hp = self.total_hp

        self.total_atk = self.stats["atk"] * (1 + self.stats["atk_per"]) + self.stats["atk_flat"]

        self.total_def = self.stats["defe"] * (1 + self.stats["def_per"] - self.stats["def_ignore"]) + self.stats["def_flat"]

        self.total_spd = self.stats["spd"] * (1 + self.stats["spd_per"]) + self.stats["spd_flat"]

        self.dot_dmg_boost = kwargs.get('dot_dmg_boost', 0.0)
        self.dot_dmg_taken = kwargs.get('dot_dmg_taken', 0.0)

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

        self.observer = observer

    def __str__(self) -> str:
        '''String'''
        return f"{self.name}"

    def __repr__(self) -> str:
        '''repr'''
        return self.__str__()
