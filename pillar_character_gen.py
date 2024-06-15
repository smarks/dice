from main import roll_dice
from enum import Enum


class BaseTypes(Enum):
    MENTAL = "Mental"
    PHYSICAL = "Physical"


class RaceTypes(Enum):
    """
    - [Humans](# "Character Races") roll 4 d8 pick two
    - [Elves](# "Character Races") roll 6 d6 pick two
    - [Dwarves](# "Character Races") roll 6 d6 pick two and add +3 for physical and -2 for mental
    - [Gnomes](# "Character Races") 4 d6  and pick two
    """
    HUMAN = [2, 8, 0, 0]  # number of rolls, side of die, physical modifier, mental modifier
    ELF = [6, 6, 0, 0]
    DWARF = [6, 6, 3, -2]

""" 
   attribute modifier dictionary 
   key - attribute 
   value - malus or bonus or 0 
   
       |        |           |
       | ------ | --------- |
       | 0-2    | Paralyzed |
       | 3      | -4        |
       | 4      | -3        |
       | 5      | -2        |
       | 6      | -1        |
       | 7 - 14 | 0         |
       | 15-16  | +1        |
       | 17     | +2        |
       | 18     | +3        |

       :return: some of str, con, and dex modifiers
       """
modifiers = {3: -4, 4: -3, 5: -2, 6: -1, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 1, 16: 1,
             17: 2, 18: 3, 19: 4, 20: 5, 21: 6, 22: 7, 23: 8, 24: 9}


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

        # calculated stats
        self.starting_skill_points = self.physical_base + self.mental_base
        self.action_point_base = 6 + self.get_physical_attribute_modifiers()
        self.hit_points = self.strength + self.constitution
        self.fatigue_points = self.constitution + self.dexterity + self.wisdom
        self.movement = self.strength + self.dexterity + self.constitution

        # nothing less than 3, anything over 18 converts to decimal increments e.g. 19 -> 18.1
        self.strength = cap(self.strength)
        self.intelligence = cap(self.intelligence)
        self.wisdom = cap(self.wisdom)
        self.dexterity = cap(self.dexterity)
        self.constitution = cap(self.constitution)
        self.personality = cap(self.personality)
        self.level = 0
        self.total_skill_points = self.starting_skill_points

    def get_physical_attribute_modifiers(self):
        """
        return an
       """
        return modifiers[int(self.strength)] + modifiers[int(self.dexterity)] + modifiers[
            int(self.constitution)]

    def get_intellectual_attribute_modifiers(self):
        """
        return an
       """
        return modifiers[int(self.intelligence)] + modifiers[int(self.wisdom)] + modifiers[
            int(self.personality_modifier)]

    def __str__(self):
        return (f"Character race: {self.race.name.capitalize()}\n"
                f"Physical base: {self.physical_base}, Mental base: {self.mental_base} (rolls: {self.base_rolls} )  Base priority: {self.base_preference.value}\n"
                f"Strength: {self.strength} (rolls: {self.strength_rolls}) base: {self.physical_base}\n"
                f"Intelligence: {self.intelligence} (rolls: {self.intelligence_rolls}) base: {self.mental_base}\n"
                f"Wisdom: {self.wisdom} (rolls: {self.wisdom_rolls}) base: {self.mental_base}\n"
                f"Dexterity: {self.dexterity} (rolls: {self.dexterity_rolls}) base: {self.physical_base}\n"
                f"Constitution: {self.constitution} (rolls: {self.constitution_rolls}) base: {self.physical_base}\n"
                f"Personality: {self.personality} (rolls: {self.personality_rolls}  base: {self.personality_modifier}\n"
                f"Level: {self.level} \n"  
                f"Hit Points: {self.hit_points} \n"
                f"Fatigue Points: {self.fatigue_points} \n"
                f"Starting Skill Points: {self.starting_skill_points} \n"
                f"Total Skill Points: {self.total_skill_points} \n"
                f"Action Points (before skill modifier) {self.action_point_base} \n"
                f"Movement: {self.movement} \n")

    def level_up(self, level: int = 1) -> None:
        for x in range(level):
            self.level += 1
            hit_point_roll = roll_dice(6,1  )
            self.hit_points += hit_point_roll[0] + modifiers[self.constitution]
            fatigue_point_roll = roll_dice(6,1  )
            self.fatigue_points += fatigue_point_roll[0] + modifiers[self.constitution]
            self.total_skill_points += self.level

def cap(attribute):
    """ if attribute is greater than 18 use old school D&D where you need 10 additional points to get to next
        attribute level

        e.g
        str 20
        20 - 18  = 2
        str == 18.2

        if attribute is 3 or less,then keep 3 amd call it 'interesting'

    """
    if attribute < 3:
        return 3

    if attribute < 18:
        return attribute

    return ((attribute - 18) / 10) + 18


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


def print_character(character):
    print("Name: ______________")
    print("Age: _____")
    print("")
    print("Description: ______________")

    print("")
    print(character)
    print("")

    print("Skills")
    print("____________________________________________________________________________")
    print("____________________________________________________________________________")

    print("")

    print("Weapons")
    print("")
    print("Type:________ Min Reach:________ Max Reach:_______ Damage:___________ % Break______")
    print("[ hit ][ crit ]:  AC 0 [  ][  ]  AC 1 [  ][  ] AC 2 [  ][  ] AC 3 [  ][  ] AC 4 [  ][  ]")
    print("")
    print("Type:________ Min Reach:________ Max Reach:_______ Damage:___________ % Break______")
    print("[ hit ][ crit ]:  AC 0 [  ][  ]  AC 1 [  ][  ] AC 2 [  ][  ] AC 3 [  ][  ] AC 4 [  ][  ]")
    print("")
    print("Type:________ Min Reach:________ Max Reach:_______ Damage:___________ % Break______")
    print("[ hit ][ crit ]:  AC 0 [  ][  ]  AC 1 [  ][  ] AC 2 [  ][  ] AC 3 [  ][  ] AC 4 [  ][  ]")
    print("")
    print("Type:________ Min Reach:________ Max Reach:_______ Damage:___________ % Break______")
    print("[ hit ][ crit ]:  AC 0 [  ][  ]  AC 1 [  ][  ] AC 2 [  ][  ] AC 3 [  ][  ] AC 4 [  ][  ]")
    print("")
    print("Armour  AC:[  ] ")
    print("")
    print(" Head:  __________________________ Torso __________________________")
    print(" Arms   __________________________ Legs  __________________________")
    print("")
    print("Notes")
    print("____________________________________________________________________________")
    print("____________________________________________________________________________")
    print("____________________________________________________________________________")
    print("____________________________________________________________________________")
    print("____________________________________________________________________________")

    print(chr(12), end='')


if __name__ == "__main__":
    elf = Character(RaceTypes.ELF, BaseTypes.PHYSICAL)
    print(elf)
    elf.level_up(4)
    print(elf)
"""
        print_character(Character(RaceTypes.ELF, BaseTypes.PHYSICAL))
        print_character(Character(RaceTypes.ELF, BaseTypes.MENTAL))
        print_character(Character(RaceTypes.DWARF, BaseTypes.PHYSICAL))
        print_character(Character(RaceTypes.DWARF, BaseTypes.MENTAL))
        print_character(Character(RaceTypes.HUMAN, BaseTypes.PHYSICAL))
        print_character(Character(RaceTypes.HUMAN, BaseTypes.MENTAL))
"""

'''
print(Character(RaceTypes.ELF, BaseTypes.PHYSICAL))
print(Character(RaceTypes.ELF, BaseTypes.MENTAL))
print(Character(RaceTypes.DWARF, BaseTypes.PHYSICAL))
print(Character(RaceTypes.DWARF, BaseTypes.MENTAL))
print(Character(RaceTypes.HUMAN, BaseTypes.PHYSICAL))
print(Character(RaceTypes.HUMAN, BaseTypes.MENTAL))

'''