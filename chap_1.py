from random import choice

cave_numbers = range(1, 21)
wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location or
       player_location == wumpus_friend_location):
    player_location = choice(cave_numbers)

print "\nWelcome to Hunt The Wumpus!!!"
print "From where you stand\nYou can see {} caves".format(len(cave_numbers))
print "To start playing, enter a number\nfor the cave you wish to enter next"


while True:
    print "You are in cave {} presently" .format(player_location)
    if (player_location == wumpus_location -1 or
        player_location == wumpus_location + 1):
        print "I smell a wumpus!!!"

    if (player_location == wumpus_friend_location -1 or
        player_location == wumpus_friend_location +1):
        print "I smell something different"

    print "Which cave next?"
    player_input = raw_input(">")
    if (not player_input.isdigit() or
        int(player_input) not in cave_numbers):
        print "{} is not a cave!!!".format(player_input)

    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
            print "Arrgh you got eaten by the wumpus!!!!"
            break
        if player_location == wumpus_friend_location:
            print "Something else ate me"
            break