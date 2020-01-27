#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random 
class Character:
    def __init__(self, name, health, power, probability):
        self.health=health
        self.power=power
        self.name=name
        self.probability = probability
   
    def attack(self, other_character):
        if(random.random()<=self.probability):
            damage=self.power*2
            print("Goku did double damage ")
        else:
            damage=self.power*1
        other_character.health -= damage
        print(f'{self.name} does this much {damage}')
    def Alive (self):
        if(self.health>0):
            return True
        else:
            return False
    
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))      

    def theHealth(self):
        if (random.random()<=self.probability):
            characterHealth=

class Hero(Character):
    def __init__(self, name, health, power, probability):
        super().__init__(name, health, power, probability)


class Goblin(Character):
    def __init__(self, name, health, power, probability):
        super().__init__(name, health, power, probability)

class theMedic(Character):
    def __init__(self, name, health, power, probability):
        super().__init__(name, health, power, probability)
class Shadow(Character):
    def shadow_health:
        if(random.random() <= self.probability):
            self.health+
Goku=Hero ("Goku", 15, 14, 0.2)
Cell=Goblin ("Cell", 20, 13, .0)
Medic=theMedic ("korin", 25, 20, 0.2)
shadow = Shadow("shadow" 1, 20, .1)




def main():
    while Cell.Alive() and Goku.Alive():
        Goku.print_status()
        Cell.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            Goku.attack(Cell)
            if Cell.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if Cell.health > 0:
            # Goblin attacks hero
           Cell.attack(Goku)
        if Goku.health <= 0:
            print("You are dead.")

main()


