class Adventurer:
    def __init__(self, name, hp, attack, defense, wisdom):
        self.name = name
        self._hp = hp
        self._max_hp = hp
        self.attack = attack
        self.defense = defense
        self.wisdom = wisdom

    @property
    def hp(self):
        return self._hp

    @property
    def max_hp(self):
        return self._max_hp

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        if actual_damage > self.hp: 
            self._hp = 0
        else:
            self._hp -= actual_damage

    def is_alive(self):
        return self.hp > 0

    def get_attack_power(self):
        return self.attack

    def heal(self, amount):
        if not self.is_alive() or amount < 0:
            print("Heal failed")
            return
        self._hp = min(self._max_hp, self._hp + amount)


class Warrior(Adventurer):
    def __init__(self, name):
        super().__init__(name, 120, 25, 15, 5)

    def get_attack_power(self):
        atk_pwr = super().get_attack_power()
        atk_pwr += 5

        return atk_pwr

class Wizard(Adventurer):
    def __init__(self, name):
        super().__init__(name, 60, 10, 5, 40)

    def cast_spell(self):
        return self.wisdom * 2

if __name__ == "__main__":
    
    merlin = Wizard("Merlin")

    print(merlin.hp)      # 60
    print(merlin.max_hp)  # 60
