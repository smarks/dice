from main import roll_dice
from enum import Enum


class BaseTypes(Enum):
    MENTAL = "mental"
    PHYSICAL = "physical"


class RaceTypes(Enum):
    """
    - [Humans](# "Character Races") roll 4 d8 pick two
    - [Elves](# "Character Races") roll 6 d6 pick two
    - [Dwarves](# "Character Races") roll 6 d6 pick two and add +3 for physical and -2 for mental
    - [Gnomes](# "Character Races") 4 d6  and pick two
    """
    HUMAN = [4, 8, 0, 0]  # number of rolls, side of die, physical modifier, mental modifier
    ELF = [6, 6, 0, 0]
    DWARF = [6, 6, 3, -2]
    GNOME = [4, 6, 0, 0]


class Character:

    def __init__(self, race, base_preference):
        self.race = race
        self.base_preference = base_preference
        self.physical_base, self.mental_base, self.base_rolls = get_bases(race, base_preference)
        self.strength_rolls, self.strength = roll_attribute(self.physical_base)
        self.intelligence_rolls, self.intelligence = roll_attribute(self.mental_base)
        self.wisdom_rolls, self.wisdom = roll_attribute(self.mental_base)
        self.dexterity_rolls, self.dexterity = roll_attribute(self.physical_base)
        self.constitution_rolls, self.constitution = roll_attribute(self.physical_base)
        self.personality_modifier = self.physical_base if self.physical_base > self.mental_base else self.mental_base
        self.personality_rolls, self.personality = roll_attribute(self.personality_modifier)

    def __str__(self):
        return (f"Character race: {self.race}  Base priority: {self.base_preference.value}\n"
                f"Physical base: {self.physical_base}, Mental base: {self.mental_base} (rolls: {self.base_rolls} )\n"
                f"Strength: {self.strength} (rolls: {self.strength_rolls}) base: {self.physical_base}\n"
                f"Intelligence: {self.intelligence} (rolls: {self.intelligence_rolls}) base: {self.mental_base}\n"
                f"Wisdom: {self.wisdom} (rolls: {self.wisdom_rolls}) base: {self.mental_base}\n"
                f"Dexterity: {self.dexterity} (rolls: {self.dexterity_rolls}) base: {self.physical_base}\n"
                f"Constitution: {self.constitution} (rolls: {self.constitution_rolls}) base: {self.physical_base}\n"
                f"Personality: {self.personality} (rolls: {self.personality_rolls}  base: {self.personality_modifier}\n")


def get_bases(race=RaceTypes.HUMAN, base_preference=BaseTypes.PHYSICAL):
    base = roll_dice(race.value[1], race.value[0])
    base.sort()

    physical_modifier = race.value[2]
    mental_modifier = race.value[3]
    index_of_highest = len(base) - 1
    if base_preference == BaseTypes.PHYSICAL:
        physical_base = base[index_of_highest] + physical_modifier
        mental_base = base[index_of_highest - 1] + mental_modifier
    else:
        physical_base = base[index_of_highest] + physical_modifier
        mental_base = base[index_of_highest - 1] + mental_modifier

    return physical_base, mental_base, base


def roll_attribute(base_modifier):
    rolls, total = roll_dice(6, 2, True)
    total = total + base_modifier
    return rolls, total


if __name__ == "__main__":
    elf = Character(RaceTypes.ELF, BaseTypes.PHYSICAL)
    print(elf)
    print("\n")

    dwarf = Character(RaceTypes.DWARF, BaseTypes.PHYSICAL)
    print(dwarf)
    print("\n")

    dwarf_thinker = Character(RaceTypes.DWARF, BaseTypes.MENTAL)
    print(dwarf_thinker)
    print("\n")

    human = Character(RaceTypes.HUMAN, BaseTypes.PHYSICAL)
    print(human)
    print("\n")

    human_mage = Character(RaceTypes.HUMAN, BaseTypes.MENTAL)
    print(human_mage)
