import random

class pig():
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

class pig_stats():
    def __init__(self):    
        self.pig = pig()
        
    def play_game(self, max_score, turn_target):
        while self.pig.piggy_bank()[1] < max_score:
            this_roll = self.pig.roll_handler()
            if self.pig.piggy_bank()[1] + this_roll[1] >= max_score: # if current rolling average puts you over the winning score, end immediately
                self.pig.end_turn(this_roll[1])
                # print('ahh victory')
            elif this_roll[0] == 1: # if a one is rolled, end turn right away and append the 0 score
                self.pig.end_turn(this_roll[1])
                # print('fuck rolled a 1')
            else: # otherwise, append the score and decide whether to keep going
                if this_roll[1] > turn_target:
                    self.pig.end_turn(this_roll[1])
                    # print('rolled a ' + str(this_roll[1]))
            
            # if self.pig.piggy_bank()[1] + this_roll[1] >= max_score:
            #     self.pig.end_turn(this_roll[1])
        
        return self.pig.piggy_bank()

    def average(self, list):
        numerator = 0
        denominator = len(list)
        print(denominator)
        for i in range(0, denominator):
            numerator += list[i-1]
            print('current num '+str(numerator))
        avg = numerator / denominator

        return avg

if __name__ == "__main__":
    pig_stats = pig_stats()

    this_game = pig_stats.play_game(100, 10)

    print(this_game[0])
    print(pig_stats.average(this_game[0]))
    # print(pig_stats.play_game(100, 4)[0])
    # target_score = 100
    # turn_target = 10
    # last_average = 0
    # cycles = 0
    # averages = []
    # print(pig.piggy_bank()[0])

    # avg = pig_stats().average(pig.piggy_bank()[0])
    # print(str(pig.piggy_bank()[0]))
    # print(avg)
