from random import random
from sys import exit


class Person(object):
    def __init__(self, name, hit_points, strength, money):
            self.name = name
            self.hit_poitns = hit_points
            self.strength  strength
            self.money = money


class Hero(Person):
    axe = False
    pickaxe = False
    bow = False
    fishingrod = False

    Hero = Person(Jacek, 0, 0, 0)
    self.food = 0

#    self.name = Jacek
#    self.hitopoins = 0
#    self.strength = 0
#    self.food = 10
#    self.money = 15

        if axe == True:
            strength += 10
        elif pickaxe == True:
            strength += 5
        elif Bow == True:
            strength += 2
        else:
            pass


class Monster(Person):
    monster1 = Person(Goblin 0, 0, 0)
    # self.name = Goblin
    # self.hitopoins = 0
    # self.strength = 0
    # self.food = 10
    # self.money = 15

class Animall(Person):
    animall1 = Person(Deer 0, 0, 0)
    # self.name = Deer
    # self.hitopoins = 0
    # self.strength = 0
    # self.food = 10
    # self.money = 15

class Fish(Person):
    fish1 = Person(Herring 0, 0, 0)
    # self.name = Crab
    # self.hitopoins = 0
    # self.strength = 0
    # self.food = 10
    # self.money = 15


class Shopkeeper(Person):
    shopkeeper = Person(Sigfrid, 0, 0, 0)
    # self.name = Sigfrid
    # self.hitopoins = 0
    # self.strength = 0
    # self.food = 10
    # self.money = 15


    def shop_greating():
        print("""
        Greeting traveller. What do you wish to have?
        1.FishingRod          - 10 gp
        2.Bow                 - 20 gp
        2 Pickaxe             - 50 gp
        4.Axe                 - 100 gp
        5. or maybe some food?-  2 gp
        """)

            buy = input("<")

            if buy == "1" and money > 10:
                fishingrod = True,
                money -= 10
            elif buy == "2" and money > 20:
                bow = True,
                money -= 20
            elif buy == "3" and money > 50:
                pickaxe = True,
                money -= 50
            elif buy == "4" and money > 100:
                axe = True,
                money -= 100
            elif buy == "5" and money > 2:
                food += 5
            elif buy == "steal"
            elif buy == "attack" or "kill"
            elif buy == "run"

            else:
            print("I dont understand")



class Location(object):
    pass


class Death(Location):

     motivation = [
        "You died. You kinda suck at this.",
        "Such a luser",
        "You're worse than your Dad's jokes."
        "Dont quit your day job"
        "I feel sorry for you... Not really"
        "Your lucky that's only a game.Though you probably also suck in life"
        ]

    def enter(self):
        print(Death.motivation[randint(0, len(self.motivation)-1)])
        exit(1)

class Forest(Location):
    pass

class Dungeon(Location):
    pass

class Lake(Location):
    pass

class Shop(Location):
    pass

class Start(Location):

    def enter(self):
        print("""
        You stand before your little house. What do you want to do?
        1. Go to the shop?
        2. Go to the lake?
        3. Go to the shop?
        4. Go to the dungeon?
        Or You just need help?(type help)
        """)

        direction = input("<")



class Engine(object):
    pass


class Battle(Engine):

    hp1 == Person(Hero).hit_points
    hp2 == Person().hit_points
    damage1 = Person(Hero).strength
    damage2 = Person().strength
    def battle(hp1, damage1, hp2, damage2):
        while hp1  > 0 or hp2 > 0:
            hp1 -= damage2 and hp2 -= damage1
