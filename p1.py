import random

mesos=0
for i in range (0,1000):
    nums=[q for q in range(1,81)]

    cards=[]
    players=[]

    for j in range (0,100):
        cards = random.sample(nums,5)
        players.append(cards)

    bingo=0
    while bingo != 1 :
        x=random.choice(nums)
        nums.remove(x)
        for k in range (1,81):
            if x in players[k]:
                players[k].remove(x)
            if players[k] == [] :
                mesos += k
                bingo = 1

print "o mesos oros arithmwn pou prepei na anagelthoun gia bingo einai: ", mesos/1000
