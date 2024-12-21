"""enemy"""

from ally_enemy_base import Enemy

if __name__ == "__main__":
    a = Enemy("Hello", 11, (5, 5, 5, 5))
    print(a.crit_rate)
