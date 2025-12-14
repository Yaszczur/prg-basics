import random

dice_roll = random.randint(1,6)
special_number = (dice_roll == 1) or (dice_roll == 6)
print('Dice roll: ', dice_roll)
print('Special number (1 or 6): ', special_number)