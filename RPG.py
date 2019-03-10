from random import random
from sys import exit


class Person(object):
    def __init__(self, name, hit_points, strength, status):
        pass

class Hero(Person):

    self.name = Jacek
    self.hitopoins = 0
    self.strength = 0
    self.status = None

        if axe == True
            strength += 10
        elif pickaxe == True
            strength += 5
        elif Bow == True:
            strength += 2
        else:
            pass


class Monster(Person):
    pass

class Animall(Person):
    pass

class Fish(Person):
    pass

class Shopkeeper(Person):

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
            if buy == "1"
            elif buy == "2"
            elif buy == "3"
            elif buy == "4"
            elif buy == "5"
            elif buy == "steal"
            elif buy == "attack" or "kill"
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



class Items(object):
    def __init__(self, name, damage, endurance)


class Backpack(Item):
    pass

class FishingRod(Items):
    pass

class Bow(Items):
    pass

class Pickaxe(Items):
    pass

class Axe(Items):
    pass

class Food(Items):
    pass

class Money(Items):
    pass


class Engine(object):


    hp1 == Person().hit_points
    hp2 == Person().hit_points
    def battle(hp1, damage1, hp2, damage2):
    while hp1 or hp2 > 0
        hp1 -= damage2 and hp2 -= damage1
