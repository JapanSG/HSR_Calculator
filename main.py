"""main"""

from ally import DestructionTrailblazer, DamageListener
import ally_enemy_base as ae
from event import EventManager
from skillpoint import SkillPoint
from turn_order_manager import TurnManager


def main():
    """Driver Code"""
    damage_listener = DamageListener()
    event_manager = EventManager()
    event_manager.attach(damage_listener)
    sp = SkillPoint()
    mc = DestructionTrailblazer(80, event_manager)
    event_manager.attach(mc)
    enemy1 = ae.Enemy("enemy1", 80, (5000, 300, 300, 100), event_manager)
    event_manager.attach(enemy1)
    turn_manager = TurnManager(sp, mc, enemy1)
    turn_manager.loop()


if __name__ == "__main__":
    main()
