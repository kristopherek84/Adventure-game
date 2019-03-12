import random
from sys import exit


class Person(object):
    def __init__(self, hit_points, strength, money):
            self.hit_poitns = hit_points
            self.strength = strength
            self.money = money




class Hero(Person):
    money = 100
    food = 0
    axe = False
    pickaxe = False
    bow = False
    fishingrod = False

    def equip(self):
        if axe == True:
            strength += 10
        elif pickaxe == True:
            strength += 5
        elif bow == True:
            strength += 2
        else:
            pass


#class Monster(Person):
goblin = Person(0, 0, 0)


#class Animall(Person):
deer = Person(0, 0, 0)


#class Fish(Person):
herring = Person(0, 0, 0)



class Shopkeeper(Person):
    alive = True

    def shop_greating(self, Hero):
        print("""
        Greeting traveller. What do you wish to have?
        1.FishingRod          - 10 gp
        2.Bow                 - 20 gp
        2 Pickaxe             - 50 gp
        4.Axe                 - 100 gp
        5. or maybe some food?-  2 gp
        """)
        buy = input("<")
        if (buy == "1" and Hero.money > 10):
            Hero.fishingrod = True
            Hero.money -= 10
        elif (buy == "2" and Hero.money > 20):
            Hero.bow = True
            Hero.money -= 20
        elif (buy == "3" and Hero.money > 50):
            Hero.pickaxe = True
            Hero.money -= 50
        elif (buy == "4" and Hero.money > 100):
            Hero.axe = True
            Hero.money -= 100
        elif (buy == "5" and Hero.money > 2):
            Hero.food += 5
        elif buy == "steal":
            pass
        elif buy == "attack" or "kill":
            pass
        elif buy == "run":
            pass
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
        print(Death.motivation[random.randint(0, len(self.motivation)-1)])
        exit(1)




class Forest(Location):

    def enter(self):
        print("""
        You enter a forest. You know that it is quite peacefull.
        But lately when you traveled to the forest you seem to notice an
        increased number of goblins in here. Forest is good hunting grounds
        but could also have an encounter with some type of monster if you
        wont be carefull
        """)



class Dungeon(Location):

    def enter(self):
        print("""
        As you traveled throgh well known forest. You noticed something which
        you didnt see before. There is a cave entrence in a place where was
        a solid rock before. Do you decide to come in?(Y/N)
        """)

dungeon = Dungeon()

class Lake(Location):

    def enter(self):
        print("You went for a stroll besiede the lakeshore.")



class Shop(Location):
    Sigfrid = Shopkeeper(0,0,0)

    def enter(self, Hero):
        if self.Sigfrid.alive == True:
            self.Sigfrid.shop_greating(Hero)
        else:
            print("""
            The shop is demolished. You dont want to spend here to
            much time. You throw a glimpse on dead shopkeeper corpse and regret
            actions which lead to slaying this poor fellow.
            """)
            enter(Start)




class Start(Location):

    def enter(self):
        print("""
        You stand before your little house. What do you want to do?
        1. Go to the shop?
        2. Go to the lake?
        3. Go to the forest?
        Or You just need help?(type help)
        """)
        hero = Hero(0, 0, 0)
        direction = input("<")
        if direction == "1":
            shop = Shop()
            shop.enter(hero)
        elif direction == "2":
            lake = Lake()
            lake.enter()
        elif direction == "3":
            forest = Forest()
            forest.enter()
        else:
            death = Death()
            death.enter()



start = Start()
start.enter()


class Engine(object):
    pass


#class Battle(Engine):

#    hp1 == Person(Hero).hit_points
#    hp2 == Person().hit_points
#    damage1 = Person(Hero).strength
#    damage2 = Person().strength
#    def battle(hp1, damage1, hp2, damage2):
#        while hp1  > 0 or hp2 > 0:
#            hp1 -= damage2,
#            hp2 -= damage1
