from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "outside"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "foyer"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "overlook"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "narrow"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "treasure"),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
commandlist = ('n', 'e', 's', 'w', 'q')


def move_player(direction, current_location):
    attribute = f'{direction}_to'
    if hasattr(room[current_location], attribute):
        return getattr(room[current_location], attribute).location
    else:
        print(f'THIS IS THE ATTRIBUTE::: {attribute}')
        return 0


# # *  Make a new player object that is currently in the 'outside' room.
player = Player('outside')

# # *  Write a loop that:
while True:

    # # * Prints the current room name
    print(f'Your Location : {player.room}')

# # * Prints the current description (the textwrap module might be useful here).
    print(room[player.room.lower()].description)

# # * Waits for user input and decides what to do.
    a = input('Which way do you want to go?  N, S, E, W or Q to quit:')


# # *  If the user enters a cardinal direction, attempt to move to the room there.
    if any(string in a for string in commandlist):
        player.room = move_player(a, player.room)
        break
# # * If the user enters "q", quit the game.
        elif direction == "q":
            print("you've ended the game")
            break
# # *  Print an error message if the movement isn't allowed.
        else:
            print('Not a valid direction, please use N, S, E, W or Q to quit.')
