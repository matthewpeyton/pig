import pig_stats

pig = pig_stats.pig()
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
