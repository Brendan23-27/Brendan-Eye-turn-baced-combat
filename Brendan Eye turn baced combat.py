# -*- coding: utf-8 -*-
"""
Brendan Eye turn baced combat 
"""
import random
class Player(object):
    def __init__(self):
        super().__init__()
        self.__player_hit_points=5
        self.__player_armor_class=2
        self.__player_hit_percent=random.randint(40,100)
        self.__player_hit_dammge=random.randint(1,4)
        
          
        @property
        def player_hit_points(self):
            return self.__player_hit_points
        
        @property
        def player_hit_percent(self):
            return self.__player_hit_percent
           
        @property
        def player_hit_dammge(self):
            return self.__player_hit_dammge 


class Monster(object):
    def __init__(self):
        super().__init__()
        self.__monster_hit_points=15
        self.__monster_hit_percent=random.randint(30,100)
        self.__hit_dammge=random.randint(1,2)
       
    @property
    def monster_hit_points(self):
        return self.__monster_hit_points
           
    @property
    def monster_hit_percent(self):
        return self.__monster_hit_percent
        
    @property
    def monster_hit_dammge(self):
        return self.__monster_hit_dammge 


def fight():
    player=Player()
    monster=Monster()
    if player.player_hit_percent>=60:
        monster.monster_hit_points -= player.player_hit_dammge
        print(f"monster was hit for {player.player_hit_dammge}")
    else:
        print("the player missed")
    if monster.monster_hit_percent>=60:
        player.player_hit_points -= monster.monster_hit_dammge
        print(f"player was hit for {monster.monster_hit_dammge}")
    else:
        print("the monster missed")
    return(player,monster)

def main():
    player=Player()
    monster=Monster()
    keep_going=True
    while(keep_going):
     fight()
     if monster.monster_hit_points<=0:
         print("you have slain your dragon good job")
         keep_going=False
     elif player.player_hit_points<=0:
        keep_going=False
main() 