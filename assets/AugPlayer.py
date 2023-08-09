VALID_SPECS = {"DeathKnight-Frost", "DeathKnight-Unholy", "DemonHunter-Havoc", "Druid-Balance", "Druid-Feral", "Evoker-Devastation", "Hunter-BeastMastery", "Hunter-Marksmanship",\
               "Hunter-Survival", "Mage-Arcane", "Mage-Fire", "Mage-Frost", "Monk-Windwalker", "Paladin-Retribution", "Priest-Shadow", "Rogue-Assasination", "Rogue-Subtlety",\
                  "Rogue-Outlaw", "Shaman-Elemental", "Shaman-Enhancement", "Warlock-Affliction", "Warlock-Demonology", "Warlock-Destruction", "Warrior-Arms", "Warrior-Fury"}


class Player:
    def __init__(self, name, ID, spec, total, dps):
        self.name = name
        self.ID = ID
        self.spec = spec
        self.total = total
        self.dps = dps

    def get_dps(self):
        return self.dps

    def __repr__(self):
        return f"Name: {self.name}, Spec: {self.spec}, Total: {self.total} DPS: {self.dps}"