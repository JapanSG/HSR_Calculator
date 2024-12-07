'''relic'''
from character import Character
import event

class Relic(object) :
    '''Relic base class'''

    class MainStat :
        '''MainStat Class'''
        def __init__(self, stat : str, num : float) -> None:
            '''Constructor'''
            self.stat = stat
            self.num = num

        def __repr__(self) -> str:
            return f"{self.stat} {self.num}"

    class SubStat :
        '''SubStat Class'''
        def __init__(self, stat : str, num : float) -> None:
            '''Constructor'''
            self.stat = stat
            self.num = num

        def __repr__(self) -> str:
            return f"{self.stat} {self.num}"

    def __init__(self, stat : str, main : float) -> None:

        self._observers = []

        self.main_stat = Relic.MainStat(stat,main)
        self.sub_stats = []
    
    def add_substats(self, **kwargs):
        '''Add substats'''
        for item in kwargs:
            self.sub_stats.append(item)
    
    def __str__(self) -> str:
        return f"Main:{self.main_stat}, {self.sub_stats}"

## Base Class
class FlatRelic(Relic) :
    '''FlatRelic Class'''

class PercentRelic(Relic) :
    '''PercentRelic Class'''

# Base Class
class Cavern(Relic) :
    '''CaverRelic Class'''

class Head(FlatRelic) :
    '''Head Class'''

class Hands(FlatRelic) :
    '''Hands Class'''

class Body(PercentRelic) :
    '''Body Class'''

class Feet(PercentRelic) :
    '''Feet Class'''

# Base Class
class Planar(Relic) :
    '''PlanarRelic Class'''

class Sphere(Planar, PercentRelic) :
    '''Planar Sphere Class'''

class Rope(Planar, PercentRelic) :
    '''Link Rope Class'''

# Champion set
class ChampionOfStreetwiseBoxing(Cavern) :
    '''Champion Of Street Wise Boxing'''
    class PassiveSubscriber:
        '''Subscriber for passive 4pc of Champion set'''
        stack = 0
        def __init__(self, ally: Character) -> None:
            '''Constructor'''
            self.ally = ally

        def update(self, lis: list):
            '''Update from event manager'''
            if lis[0] == event.DamageEvent and self.stack < 5 and (lis[1] == self.ally or lis[2] == self.ally):
                self.ally.stats['atk_per'] += 0.05
                self.stack += 1

    setid = "01"
    def passive_2pc(self, ally : Character) -> None:
        '''Activate 2pc passive'''
        ally.dmg_boost["physical"] += 0.1
    
    def passive_4pc(self, ally : Character, observer : event.EventManager) -> None:
        '''Activate 4pc passive'''
        observer.attach(self.PassiveSubscriber(ally))


class ChampionHead(ChampionOfStreetwiseBoxing, Head) :
    '''Champion Head'''

class ChampionHands(ChampionOfStreetwiseBoxing, Hands) :
    '''Champion Hands'''

class ChampionBody(ChampionOfStreetwiseBoxing, Body) :
    '''Champion Body'''

class ChampionFeet(ChampionOfStreetwiseBoxing, Feet) :
    '''Champion Feet'''

if __name__ == "__main__":
    a = ChampionBody("atk", 43.3)
    