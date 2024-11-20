'''enemy'''
from character import Character

class Enemy(Character):
    '''Enemy Class'''
    def __init__(self, name: str, base_stats : tuple, **kwargs) -> None:
        '''Constructor'''
        super().__init__(name, base_stats, **kwargs)
        
    def __str__(self):
        '''String'''
        return super().__str__()