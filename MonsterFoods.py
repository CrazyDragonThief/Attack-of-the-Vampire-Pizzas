class Monster(object):
    eats = 'food'
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name + ' speaks')
#Monster Class
    def eat(self, meal):
        if meal == self.eats:
            print('yum!')
        else:
            print('blech!')
#my_monster = Monster('Spooky Snack')
#my_monster.speak()
#my_monster.eat('food')

#Subclass of Monster
class FrankenBurger(Monster):
    eats = 'hamburger patties'
    def speak(self):
        print('My name is ' + self.name + 'Burger')

#instance of FrankenBurger
#my_frankenburger = FrankenBurger('Veggiesaurus')
#my_frankenburger.speak()
#my_frankenburger.eat('pickles')

class CrummyMummy(Monster):
    eats = 'chocolate chips'
    def speak(self):
        print('My name is ' + self.name + 'Mummy')

#my_crummymummy = CrummyMummy('Veggiesaurus')
#my_crummymummy.speak()
#my_crummymummy.eat('pickles')

class WereWatermelon(Monster):
    eats = 'watermelon juice'
    def speak(self):
        print('My name is Were' + self.name)

#my_werewatermelon = WereWatermelon('Veggiesaurus')
#my_werewatermelon.speak()
#my_werewatermelon.eat('watermelon juice')
        
monster_selection = input('What kind of monster do you want to create? Select: frankenburger, crummymummy, or werewatermelon. ')
monster_name = input('What do you want to name your monster? ')
monster_meal = input('What will you feed your monster? ')

if monster_selection == 'frankenburger':
    monster_type = FrankenBurger
elif monster_selection == 'crummymummy':
    monster_type = CrummyMummy
elif monster_selection == 'werewatermelon':
    monster_type = WereWatermelon
else:
    monster_type = Monster

my_monster = monster_type(monster_name)
my_monster.speak()
my_monster.eat(monster_meal)
