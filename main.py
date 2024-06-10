import random


def roll_dice(sides, rolls=1, sum_array=False):
    """
    Simulates rolling a die with a specified number of sides a given number of times.

    Parameters:
    sides (int): The number of sides on the die.
    rolls (int): The number of times to roll the die.
    sum (bool): If True, returns a tuple with the list of rolls and their sum; otherwise, returns the list of rolls.

    Returns:
    tuple or list: A tuple containing the list of rolls and their sum if sum is True; otherwise, the list of rolls.
    """
    if sides not in [4, 6, 8, 10, 12, 20, 100]:
        raise ValueError("Invalid number of sides. Choose from 4, 6, 8, 10, 12, 20, or 100.")

    results = [random.randint(1, sides) for _ in range(rolls)]

    if sum_array:
        return results, sum(results)
    else:
        return results


def main():
    print("Welcome to the Dice Roller!")
    while True:
        try:
            sides = int(input("Enter the number of sides on the die (4, 6, 8, 10, 12, 20, 100 for percentile): "))
            rolls = int(input("Enter the number of rolls: "))
            results = roll_dice(sides, rolls)
            print(f"Results of rolling a {sides}-sided die {rolls} times: {results}")
        except ValueError as e:
            print(e)

        another_roll = input("Do you want to roll again? (yes/no): ").strip().lower()
        if another_roll != 'yes':
            break


if __name__ == "__main__":
    main()