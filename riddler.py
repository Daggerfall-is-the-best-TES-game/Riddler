from random import choices


trials = 100000  # the number of simulations to run
trial = 0  # the total number of pairs of cards the boy tries
for x in range(trials):
    TotalCards = 20
    cardlist = [x for x in range(int(TotalCards / 2))] * 2
    while cardlist:
        pair = choices(cardlist, k=2)
        if len(set(pair)) == 1:  # both cards match
            cardlist.remove(pair[0])
            cardlist.remove(pair[0])
        trial += 1
trial = int(trial / trials)


print("Time taken is {} seconds".format(trial * 2))
