#!/bin/python
from random import randint

friendByMember = 20 # minimum, could be more
nbMember = 10000
groupSize = 5
members = []

for i in range(nbMember):
    members.append(set())

# We create the connection between the member randomly
for i in range(nbMember):
    while len(members[i]) < friendByMember:
        choice = randint(0, nbMember - 1)
        # The connection are reciprocals
        members[i].add(choice)
        members[choice].add(i)


def crossDetection():
    # The fake account chooses randomly two groupes of people
    group1 = set()
    while len(group1) < groupSize:
        choice = randint(0, nbMember - 1)
        group1.add(choice)

    group2 = set()
    while len(group2) < groupSize:
        choice = randint(0, nbMember - 1)
        group2.add(choice)

    # We verify if a people in group1, know someone in group2
    for member in group1:
        for friend in members[member]:
            if friend in group2:
                return 1
    # If it isn’t the case, the fake account go undetected, even if each people ask each friends if he know him.
    return 0

detections = 0
for i in range(1000):
    detections += crossDetection()

print(detections/1000) # What I found empirically
print(1-(1-(friendByMember * groupSize)/nbMember)**groupSize) # What I found by a approximative calculus
