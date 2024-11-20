'''ally'''
from character import Character

class Ally(Character):
    '''Ally Class'''
    def __init__(self, name: str, base_stats: tuple, **kwargs) -> None:
        '''Constructor
            hidden_stats =  (
                            break_efficiency: float,
                            taunt: float
                            )
        '''
        super().__init__(name, base_stats, **kwargs)
        self.break_efficiency = kwargs.get('break_efficiency', 0.0)
        self.taunt = kwargs.get('taunt', 0.0)

    def __str__(self) -> str:
        '''String'''
        return super().__str__()

class DestructionTrailblazer(Ally):
    '''DestructionTrailblazer'''
    def __init__(self,**kwargs) -> None:
        name = "Trailblazer"
        base_stats = (1203,620,460,100)
        super().__init__(name, base_stats, **kwargs)

    def __str__(self) -> str:
        '''String'''
        return super().__str__()

    def basic(self, target) -> None:
        pass

if __name__ == "__main__":
    mc = DestructionTrailblazer(taunt = 125.0)
    print(mc)
