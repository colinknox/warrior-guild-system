class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount

        if self.health < 0:
            self.health = 0

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def heal(self, amount):
        self.health += amount

class Warrior(Hero):
    def __init__(self, name, health, stamina):
        super().__init__(name, health)
        self.__stamina = stamina

    def power_attack(self, target):
        if self.__stamina >= 20:
            self.__stamina -= 20
            target.take_damage(30)
        else:
            raise Exception("Not enough stamina")

    def get_stamina(self):
        return self.__stamina
    
    def rest(self):
        self.__stamina += 10

class EliteWarrior(Warrior):
    def __init__(self, name, health, stamina):
        super().__init__(name, health, stamina)
        self.__num_victories = 0

    def power_attack(self, target):
        super().power_attack(target)

        if target.is_alive() == False:
            self.__num_victories += 1

    def get_victories(self):
        return self.__num_victories

    def is_veteran(self):
        if self.__num_victories >= 5:
            return True
        else:
            return False

class Mage(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.__mana = mana

    def cast_fireball(self, target):
        if self.__mana >= 30:
            self.__mana -= 30
            target.take_damage(40)
        else:
            raise Exception("Not enough mana")

    def get_mana(self):
        return self.__mana

    def meditate(self):
        self.__mana += 20
