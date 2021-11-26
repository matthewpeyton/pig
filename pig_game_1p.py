import random

class pig_game():
    def __init__(self):
        self.total = 0
        self.bank = []
        self.current_score = 0

    def end_turn(self, num):
        self.total += self.current_score
        self.bank.append(self.current_score)
        self.current_score = 0

    def roll(self, num): # returns random number between 1 and number
        this_roll = random.randrange(1, num)
        return this_roll

    def roll_handler(self): # returns a roll and a turn score as a tuple (first element is the roll, second is the turn total)
        last_roll = self.roll(6)
        if last_roll != 1:
            self.current_score += last_roll
        else: self.current_score = 0
        return last_roll, self.current_score

    def piggy_bank(self):
        return self.bank, self.total

    def new_game(self):
        self.total = 0
        self.bank = []
        self.current_score = 0

if __name__ == "__main__":
    pig = pig_game()
    target_score = 100
    while pig.piggy_bank()[1] < target_score:
        this_roll = pig.roll_handler()
        if pig.piggy_bank()[1] + this_roll[1] >= target_score:
            print('You rolled a ' + str(this_roll[0]))
            pig.end_turn(this_roll[1])
        elif this_roll[0] == 1:
            input('You rolled a 1 and ended your turn. Your existing total is ' + str(pig.piggy_bank()[1]))
            pig.end_turn(this_roll[1])
        else:
            rollq = input('You rolled a ' + str(this_roll[0]) + ' and now have ' + str(this_roll[1]) + ' points. Your existing total is ' + str(pig.piggy_bank()[1]) + '. Do you want to "roll" or "stay"?')
            if rollq == 'stay':
                pig.end_turn(this_roll[1])
        
        if pig.piggy_bank()[1] + this_roll[1] >= target_score:
            pig.end_turn(this_roll[1])

    print('You won with a score of ' + str(pig.piggy_bank()[1]) + '!')
            