# roll 4d get highest two
import math

from main import roll_dice
from enum import Enum


class BaseTypes(Enum):
    MENTAL = 1
    PHYSICAL = 2


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


def get_bases(race=RaceTypes.HUMAN, base_preference=BaseTypes.PHYSICAL):
    print(race)
    base = roll_dice(race.value[1], race.value[0])
    base.sort()
    print(f"rolled: D{race.value[1]} {race.value[0]} times  {base} ")

    physical_modifier = race.value[2]
    print(f"physical modifier: {physical_modifier}")
    mental_modifier = race.value[3]
    print(f"mental modifier: {mental_modifier}")
    index_of_highest = len(base) - 1
    if base_preference == BaseTypes.PHYSICAL:
        print("A higher physical base is preferred.")
        physical_base = base[index_of_highest] + physical_modifier
        mental_base = base[index_of_highest - 1] + mental_modifier
    else:
        print("A higher mental base is preferred.")
        physical_base = base[index_of_highest] + physical_modifier
        mental_base = base[index_of_highest - 1] + mental_modifier

    return physical_base, mental_base


def roll_attribute(base_modifier):
    rolls, total = roll_dice(6, 2, True)
    total = total + base_modifier
    return rolls, total


if __name__ == "__main__":
    physical_base, mental_base = get_bases(RaceTypes.HUMAN, BaseTypes.PHYSICAL)
    print(f"Physical: {physical_base}")
    print(f"Mental: {mental_base}")
    strength_rolls, strength = roll_attribute(physical_base)
    print(f"Strength: {strength} {strength_rolls}  + physical base {physical_base}")
    intelligence_rolls, intelligence = roll_attribute(mental_base)
    print(f"Intelligence: {intelligence} {intelligence_rolls} + mental base {mental_base}")
    wisdom_rolls, wisdom = roll_attribute(mental_base)
    print(f"Wisdom: {wisdom} {wisdom_rolls} + mental base {mental_base}")
    dex_rolls, dex = roll_attribute(physical_base)
    print(f"Dex: {dex} {dex_rolls} + physical base {physical_base}")
    personality_modifier = physical_base if physical_base > mental_base else mental_base
    personality_rolls, personality = roll_attribute(personality_modifier)
    print(f"Per: {personality} {personality_rolls} + personality_modifier {personality_modifier}")
    print("\n")
    print("\n")

    physical_base, mental_base = get_bases(RaceTypes.DWARF, BaseTypes.PHYSICAL)
    print(f"Physical: {physical_base}")
    print(f"Mental: {mental_base}")
    strength_rolls, strength = roll_attribute(physical_base)
    print(f"Strength: {strength} {strength_rolls}  + physical base {physical_base}")
    intelligence_rolls, intelligence = roll_attribute(mental_base)
    print(f"Intelligence: {intelligence} {intelligence_rolls} + mental base {mental_base}")
    wisdom_rolls, wisdom = roll_attribute(mental_base)
    print(f"Wisdom: {wisdom} {wisdom_rolls} + mental base {mental_base}")
    dex_rolls, dex = roll_attribute(physical_base)
    print(f"Dex: {dex} {dex_rolls} + physical base {physical_base}")
    personality_modifier = physical_base if physical_base > mental_base else mental_base
    personality_rolls, personality = roll_attribute(personality_modifier)
    print(f"Per: {personality} {personality_rolls} + personality_modifier {personality_modifier}")
    print("\n")
    print("\n")

    physical_base, mental_base = get_bases(RaceTypes.HUMAN, BaseTypes.MENTAL)
    print(f"Physical: {physical_base}")
    print(f"Mental: {mental_base}")
    strength_rolls, strength = roll_attribute(physical_base)
    print(f"Strength: {strength} {strength_rolls}  + physical base {physical_base}")
    intelligence_rolls, intelligence = roll_attribute(mental_base)
    print(f"Intelligence: {intelligence} {intelligence_rolls} + mental base {mental_base}")
    wisdom_rolls, wisdom = roll_attribute(mental_base)
    print(f"Wisdom: {wisdom} {wisdom_rolls} + mental base {mental_base}")
    dex_rolls, dex = roll_attribute(physical_base)
    print(f"Dex: {dex} {dex_rolls} + physical base {physical_base}")
    personality_modifier = physical_base if physical_base > mental_base else mental_base
    personality_rolls, personality = roll_attribute(personality_modifier)
    print(f"Per: {personality} {personality_rolls} + personality modifier {personality_modifier}")

    physical_base, mental_base = get_bases(RaceTypes.ELF, BaseTypes.MENTAL)
    print(f"Physical: {physical_base}")
    print(f"Mental: {mental_base}")
    strength_rolls, strength = roll_attribute(physical_base)
    print(f"Strength: {strength} {strength_rolls}  + physical base {physical_base}")
    intelligence_rolls, intelligence = roll_attribute(mental_base)
    print(f"Intelligence: {intelligence} {intelligence_rolls} + mental base {mental_base}")
    wisdom_rolls, wisdom = roll_attribute(mental_base)
    print(f"Wisdom: {wisdom} {wisdom_rolls} + mental base {mental_base}")
    dex_rolls, dex = roll_attribute(physical_base)
    print(f"Dex: {dex} {dex_rolls} + physical base {physical_base}")
    personality_modifier = physical_base if physical_base > mental_base else mental_base
    personality_rolls, personality = roll_attribute(personality_modifier)
    print(f"Per: {personality} {personality_rolls} + personality modifier {personality_modifier}")
