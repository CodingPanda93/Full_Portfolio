coin = 0
head = 0
tail = 0
for count in range(1,5000):
    import random
    random_num = random.random()
    coin = round(random_num)
    if (coin==0):
        head = head + 1
        print "Attempt# {} :Throwing a coin... It's a head!...Got {} head(s) so far and {} tail(s) so far".format(count, head, tail)
    else:
        tail = tail + 1
        print "Attempt# {} :Throwing a coin... It's a tail!...Got {} head(s) so far and {} tail(s) so far".format(count, head, tail)
print "Ending the program. Thank you!"
