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
                print('You rolled a 1 and lost '+ str(self.turn_total) + " points")
                self.turn_total = 0
                self.bank.append(self.turn_total)
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

    def reinitialize(self):
        self.total = 0
        self.bank = []


class pig_stats():
    def average(self, list):
        numerator = 0
        denominator = len(list)
        for i in (0, denominator):
            numerator = numerator + list[i-1]
        avg = numerator / denominator

        return avg

if __name__ == "__main__":
    pig = pig()
    last_average = 0
    cycles = 0
    averages = []
    for i in range(1, 100):
        print(i)
        pig.piggy_total(100,20)
        averages.append(pig_stats().average(pig.print_bank()))
        print(pig.print_bank)
        pig.reinitialize()
    print(str(averages))
    total_avg = pig_stats().average(averages)
    print(total_avg)
