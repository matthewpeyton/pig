import random
class pig():
    def __init__(self):
        self.total = 0
        self.bank = []

    def roll(self, num): # returns random number between 1 and number
        this_roll = random.randrange(1, num)
        return this_roll

    def target(self, target):
        self.turn_total = 0
        while self.turn_total < target:
            fresh_roll = self.roll(6)
            if fresh_roll == 1:
                # print('You rolled a 1 and lost '+ str(self.turn_total) + " points")
                self.turn_total = 0
            else:
                self.turn_total = self.turn_total + fresh_roll
        self.piggy_bank(self.turn_total)
        return self.turn_total

    def piggy_total(self, num, target):
        while self.total < num:
            rolling = self.target(target)
            self.total = self.total + rolling
            # print("Rolling total: " + str(self.total))
        return self.total

    def piggy_bank(self, num):
        self.bank.append(num)

    def print_bank(self):
        return self.bank

    def average(self):
        numerator = 0
        denominator = len(self.bank)
        for i in (0,denominator):
            numerator = numerator + self.bank[i-1]
        denominator = len(self.bank)
        avg = numerator / denominator
        
        return avg

    def reinitialize(self):
        self.total = 0
        self.bank = []

if __name__ == "__main__":
    pig = pig()
    last_average = 0
    cycles = 0
    while last_average < 10:
        pig.piggy_total(100,20)
        last_average = pig.average()
        pig.reinitialize()
        cycles += 1
    print(last_average)
    print(cycles)
    