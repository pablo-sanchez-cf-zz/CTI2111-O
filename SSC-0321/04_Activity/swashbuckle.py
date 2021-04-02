# Pablo Sanchez
# python 2.7.16
# Milestone 1

'''This is a typical Paper, Rock, Scissors game, 
that is played using Dodge, Parry, Thrust instead.
Dodge beats Parry > Parry beats Thrust > Thrust beats Dodge'''

# Import the random Module
import random

# Here are your list of Pirates
pirates = [
    'Captain William Kidd',
    'Pierre Le Grand',
    'Red Leg Grieves',
    'Edward Low',
    'Calico Jack Rackham',
    'Anne Bonny',
    'Captain Henry Morgan',
    'Black Sam Bellamy',
    'Black Bart Roberts',
    'Edward Blackbeard Teach']

print ("The Pirates are: " + str(pirates))

#  Attacks List
attack = ['dodge', 'parry', 'thrust']

print ("Pirates can use the following Attacks: " + str(attack))

# Choosing the Characters for the fight
player = random.choice(pirates)
opponent = random.choice(pirates)

print "Ahoy ye swabs! Prepare for battle!"
print "The Player ("+ player + ") has challenged the Opponent (" + opponent + ") in one on one combat!"

# Choosing the attack
pattack = random.choice(attack)
oattack = random.choice(attack)
print "*** " + player + " attacks with: " + pattack.upper()
print "*** " + opponent + " attacks with: " + oattack.upper()

# Game Results

if pattack == oattack:
    winner = "There is no Winner. It is a tie!"
elif pattack == "dodge" and oattack == "parry":
    winner = "Winner is: " + player
elif pattack == "arry" and oattack == "dodge":
    winner = "Winner is: " + opponent
elif pattack == "parry" and oattack == "thrust":
    winner = "Winner is: " + player
elif pattack == "thrust" and oattack == "parry":
    winner = "Winner is: " + opponent
elif pattack == "thrust" and oattack == "dodge":
    winner = "Winner is: " + player
elif pattack == "dodge" and oattack == "thrust":
    winner = "Winner is: " + opponent

print "The Winner is: " + winner