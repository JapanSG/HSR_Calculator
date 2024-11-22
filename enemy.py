'''enemy'''
from character import Character

class Enemy(Character):
    '''Enemy Class'''
    def __init__(self, name: str, base_stats : tuple, **kwargs) -> None:
        '''Constructor'''
        super().__init__(name, base_stats, **kwargs)
        self.crit_rate = 0

    def __str__(self):
        '''String'''
        return super().__str__()
    
if __name__ == "__main__":
    a = Enemy("Hello",(5,5,5,5))
    print(a.crit_rate)
