import random

class Dice:
    
    def __init__(self) -> None:
        self.dice_value = None
        
    def roll_dice(self):
        self.dice_value = random.choice(range(1,7))
        return self.dice_value
    
    def simulator(self, dice_value):
        
        if dice_value == 1:
            print('''
            +-------+
            |       |
            |   ●   |
            |       |
            +-------+
            ''')
            
        elif dice_value == 2:
            print('''
            +-------+
            | ●     |
            |       |
            |     ● |
            +-------+
            ''')
            
        elif dice_value == 3:
            print('''
            +-------+
            | ●     |
            |   ●   |
            |     ● |
            +-------+
            ''')
            
        elif dice_value == 4:
            print('''
            +-------+
            | ●   ● |
            |       |
            | ●   ● |
            +-------+
            ''')
            
        elif dice_value == 5:
            print('''
            +-------+
            | ●   ● |
            |   ●   |
            | ●   ● |
            +-------+
            ''')
            
        elif dice_value == 6:
            print('''  
            +-------+
            | ●   ● |
            | ●   ● |
            | ●   ● |
            +-------+
            ''')

if __name__ == "__main__":
    
    dice = Dice()
    print("Rolling Dice :)")
    roll = True
    while roll:
        
        dice_value = dice.roll_dice()
        dice.simulator(dice_value)
        
        if input("Roll Again? y/n : ").lower() != 'y':
            roll=False