import random

class pig():
    def __init__(self):
        self.total = 0
        self.bank = []
        self.current_score = 0

    def end_turn(self, num): # append current_score to the bank and reset it to 0
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

    def piggy_bank(self): # returns the list of turn results and the total score
        return self.bank, self.total

    def new_game(self): # start a new game - return all values to 0/null
        # couldn't I just run __init__ again??
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

        return self.pig.piggy_bank()

    def average(self, list):
        numerator = 0
        denominator = len(list)
        for i in range(0, denominator):
            numerator += list[i-1]
        avg = numerator / denominator

        return avg

    def new_game(self):
        self.pig.new_game()

if __name__ == "__main__":
    pig_stats = pig_stats()

    averages = []
    iteration = 0
    iterations = 100000 # how many games do you want to average out?

    while iteration < iterations:
        this_game = pig_stats.play_game(100, 9)
        pig_stats.new_game()
        averages.append(pig_stats.average(this_game[0]))
        iteration += 1
        if iteration % 10000 == 0:
            print("That's another 10000 iterations done.")

    print(pig_stats.average(averages))
