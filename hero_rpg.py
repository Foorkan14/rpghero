#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random 
class Character:
    def __init__(self, name, health, power, probability, evasion,):
        self.health=health
        self.power=power
        self.name=name
        self.probability = probability
        self.evasion = evasion
    def attack(self, other_character):
        if(other_character.name == "shadow"):
            if  random.randint(1, 10) == 1:
                other_character.health -= self.power
        if(random.random()<=self.probability):
            damage=self.power*2
            print("Goku did double damage ")
        else:
            damage=self.power*1
        other_character.health -= damage
        print(f'{self.name} does this much {damage} damage, and you have earned this much in your account {self.account}')
    def Alive (self):
        if(self.health>0):
            return True
        else:
            return False
    
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))      

    def theHealth(self):
        return (self.health)
    
    def bank_account(self, other_character):
        self.account += other_character.bounty


class Hero(Character):
    def __init__(self, name, health, power, probability, evasion,):
        super().__init__(name, health, power, probability, evasion,)
        self.account=0
        


class Goblin(Character):
    def __init__(self, name, health, power, probability, evasion,):
        super().__init__(name, health, power, probability, evasion,)
        self.account=0
        self.bounty=5
        

class theMedic(Character):
    def __init__(self, name, health, power, probability, evasion,):
        super().__init__(name, health, power, probability, evasion,)
        self.account=0
        self.bounty=10
        def medic_health(self):
            if(random.random() <= self.probability):
                self.health +=2
                print("health recuperated ")
            else:
                print("health did not recuperate ")
        def attack(self, other_character):
            self.medic_health()
            super().attack(other_character)

class Shadow(Character):
    def __init__(self, name, health, power, probability, evasion,):
        self.name = "shadow"
        self.account=0
        self.bounty=10
        super().__init__(name, health, power, probability, evasion,)
        if(random.randint(1, 10) == 1):
            pass
            

class Zombie(Character):
    def __init__(self, name, health, power, probability, evasion,):
        self.name="zombie"
        self.account=0
        self.bounty=20
        super().__init__(name, health, power, probability, evasion,)
        # def attack(self):
        #     if(other_character.name == "zombie"):
        #         if(self.health<0):
        #             return True
Goku=Hero ("Goku", 15, 14, 0.2, 0.0,)
Cell=Goblin ("Cell", 20, 10, .0, 0.0,)
Medic=theMedic ("korin", 25, 5, 0.2, 0.0,)
shadow = Shadow("shadow", 1, 20, .1, 0.9,)
zombie = Zombie("zombie", 10, 10, 0.0, 0.0,)



def main():
    while Cell.Alive() and Goku.Alive():
        Goku.print_status()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. fight medic")
        print("3. fight shadow")
        print("4. fight zombie")
        print("5. do nothing")
        print("6. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            Goku.attack(Cell)
            if Cell.health <= 0:
                print("The goblin is dead. You have won 5 coins! ")

        elif raw_input == "2":
            Goku.attack(Medic)
            if Medic.health <= 0:
                print("medic is dead. You have won 10 coins! ")
        elif raw_input == "3":
            Goku.attack(shadow)
            if shadow.health <=0:
                print("you have defeated shadow! You have won 20 coins!  ")
        elif raw_input == "4":
            Goku.attack(zombie)
            if zombie.health <=0:
                print("He is still alive! You have won nothing! ")
        elif raw_input == "5":
            pass
        elif raw_input == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if raw_input == "1":
            if Cell.health > 0:
                # Goblin attacks hero
                Cell.attack(Goku)
                Cell.print_status()
            if Goku.health <= 0:
                print("You are dead.")
        elif raw_input == "2":

            if Medic.health <= 0:
                print("medic is dead. ")
            else:
                Medic.attack(Goku)
                Medic.print_status()
        elif raw_input == "3":
            if shadow.health <=0:
                print("you have defeated shadow! ")
            else:
                shadow.attack(Goku)
                shadow.print_status()
        elif raw_input == "4":
            if zombie.health <= 0:
                zombie.attack(Goku)
                zombie.print_status()
                print("i ran! ")
            else: 
                print("He is still alive! ")
            

        

# zombie.attack(Goku)
main()

