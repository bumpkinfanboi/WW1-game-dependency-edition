import string
import functions
import introsequence
import os
import keyboard
import json
import math

difficulty = ""
class player:
    def __init__(self):
        self.position = {} #figure that out
        self.inventory = [] # multiple bags (also equip slots?)
    def intro(self):
        global difficulty
        introOutput = introsequence.start()
        self.stats = introOutput["stats"]
        self.perks = introOutput["perks"]
        self.inventory = introOutput["inventory"]
        difficulty = introOutput["difficulty"]
    def getHPTotal(self, outof=False):
        running_total = 0
        for i in self.stats["health"]:
            running_total += self.stats["health"][i]
        if outof == True:
            print(str(running_total) + "/" + str(self.stats["health_max"]["total"]))
            return running_total, self.stats["health_max"]["total"]
        else:
            print(running_total)
            return running_total
    def damage_organ(self, organ, amount):
        if amount > self.stats["health"][organ]:
            self.stats["health"][organ] = 0
            print("ORGAN " + str(organ) + " NOW HAS 0 HEALTH")
            print(str(organ) + " has " + str(self.stats["health"][organ]) + " health")
        elif -self.stats["health_max"][organ] > amount:
            self.stats["health"][organ] = self.stats["health_max"][organ]
            print("ORGAN " + str(organ) + " HAS " + str(self.stats["health"][organ]))
        else:
            print("AMOUNT = "+ str(amount))
            print("OLD HEALTH = " + str(self.stats["health"][organ]))
            self.stats["health"][organ] -= amount
            print("NEW HEALTH = " + str(self.stats["health"][organ]))
    #def manage_inventory(self, item, action, amount=None):

class container:
    def __init__(self, max_cap, weight_reduction = None, difficulty_scaled=False,):
        global difficulty
        self.items_contained = []
        if difficulty_scaled == True:
            if difficulty == "easy":
                _diff_mult = 1.3
            elif difficulty == "medium":
                _diff_mult = 1
            elif difficulty == "hard":
                _diff_mult = 0.8
            else:
                print("Container calss can't find difficulty! Defaulting to 1!")
                _diff_mult = 1
            self.max_capacity = math.ceil(max_cap * _diff_mult)
        else: self.max_capacity = max_cap
        if weight_reduction == None:
            self.encumbrance_mult = 1
        else:
            self.encumbrance_mult = weight_reduction
    def checkmaxcap(self):
        _counter = 0
        for i in self.items_contained:
            i["weight"]*self.encumbrance_mult += _counter
        if _counter > self.max_capacity:
            print("OVERCAP!!") # TODO: add something there besides a print error
        return _counter
    #def use_container(self, item, add_or_remove):


user = player()
user.intro()