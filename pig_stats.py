import random

class pig():
    def __init__(self):
        self.total = 0
        self.bank = []
        self.current_score = 0

    def end_turn(self): # append current_score to the bank and reset it to 0
        self.total += self.current_score
        self.bank.append(self.current_score)
        self.current_score = 0

    def roll(self, num=6): # returns random number between 1 and number
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

    def play_game(self, turn_target=10, max_score=100):
        while self.pig.piggy_bank()[1] < max_score:
            this_roll = self.pig.roll_handler()
            if self.pig.piggy_bank()[1] + this_roll[1] >= max_score: # if current rolling average puts you over the winning score, end immediately
                self.pig.end_turn()
                # print('ahh victory')
            elif this_roll[0] == 1: # if a one is rolled, end turn right away and append the 0 score
                self.pig.end_turn()
                # print('fuck rolled a 1')
            else: # otherwise, append the score and decide whether to keep going
                if this_roll[1] > turn_target:
                    self.pig.end_turn()
                    # print('rolled a ' + str(this_roll[1]))

        return self.pig.piggy_bank()

    def average(self, list):
        numerator = 0
        denominator = len(list)
        for i in range(0, denominator):
            numerator += list[i-1]
        avg = numerator / denominator

        return avg

    def iterate(self, target_score, iterations=1000000):
        averages = [] # empty array for averages to go into, for averaging the averages later
        turns = [] # empty array for number of turns to go into, for averaging the game lengths later
        iteration = 0

        while iteration < iterations:
            this_game = self.play_game(target_score)
            self.new_game()
            averages.append(self.average(this_game[0]))
            turns.append(len(this_game[0]))
            iteration += 1
            # if iteration % 100000 == 0: # every hundred thousand games, print a message to the screen
            #     print("That's " + str(iteration) + " games done.")
            # elif iteration % 10000 == 0: # every ten thousand games, print a period to the screen
            #     print(".", end="", flush=True)

        turn_avg = self.average(averages)
        score_avg = self.average(turns)

        return turn_avg, score_avg

    def new_game(self):
        self.pig.new_game()

if __name__ == "__main__":
    pig_stats = pig_stats()

    results = []
    gamesPerTarget = int(input("How many games would you like to play for each target? Default is one million: ") or 1000000)

    for i in range(1, 100):
        result = pig_stats.iterate(i, gamesPerTarget)
        results.append(result)
        print("Target score was " + str(i))
        print("Average turn scored " + str(result[0]) + " points.") # return average points per turn
        print("Average game was " + str(result[1]) + " turns long") # return average number of turns

    print(str(results))