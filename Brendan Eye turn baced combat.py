# -*- coding: utf-8 -*-
"""
Brendan Eye turn baced combat 
"""
import random
class Fighter(object):
    def __init__(self, hit_points, armor, hit_percent, hit_damage):
        super().__init__()
        self.__hit_points=hit_points
        self.__armor=armor
        self.__hit_percent=hit_percent
        self.__hit_damage=hit_damage
          
    @property
    def hit_points(self):
        return self.__hit_points
   
    @hit_points.setter
    def hit_points(self, value):
        self.__hit_points = value
    
    @property
    def hit_damage(self):
        return self.__hit_damage
    
    @hit_damage.setter
    def hit_damage(value,self):
        self.__hit_damage = value
           
    @property
    def hit_percent(self):
        return self.__hit_percent
    
    @hit_percent.setter
    def hit_percent(value,self):
        self.__hit_percent = value

def fight(fighter1, fighter2):

    if fighter1.hit_percent> 60:
        fighter2.hit_points -= fighter1.hit_damage
        print(f"monster was hit for {fighter1.hit_damage}")

    elif fighter1.hit_percent<= 60:
       fighter1.hit_points -= fighter2.hit_damage
       print(f"player was hit for {fighter2.hit_damage}")
    
    if fighter2.hit_percent> 60:
        fighter2.hit_points -= fighter1.hit_damage
        print(f"monster was hit for {fighter1.hit_damage}")

    elif fighter2.hit_percent<= 60:
       fighter2.hit_points -= fighter1.hit_damage
       print(f"player was hit for {fighter2.hit_damage}")
    

def main():
    player=Fighter(100, 10, random.randint(50,100), 35)
    monster=Fighter(80, 10, random.randint(40,100), 30)
    keep_going=True
    while(keep_going):
         fight(player, monster)
         if monster.hit_points<=0:
             print("you have slain your dragon good job")
             keep_going=False
         elif player.hit_points<=0:
             print("you died")
             keep_going=False
main() 