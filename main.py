'''main'''
from ally import DestructionTrailblazer
import ally_enemy_base as ae
from event import EventManager
from skillpoint import SkillPoint
from turn_order_manager import TurnManager
def main():
    '''Driver Code'''
    event_manager = EventManager()
    sp = SkillPoint()
    mc = DestructionTrailblazer(80, event_manager)
    event_manager.attach(mc)
    enemy1 = ae.Enemy("enemy1", 80, (5000,300,300,100), event_manager)
    event_manager.attach(enemy1)
    turn_manager = TurnManager(sp ,mc, enemy1)
    turn_manager.loop()
if __name__ == "__main__":
    main()
