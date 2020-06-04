from room import Room
from player import Player
import textwrap
from item import Item


# Declare all the items

item = {
    'magic wand': Item('magic wand', """This magic wand is magical!"""),
    'gold coins': Item('gold coins', 'Gold coins for your pocket'),
    'mystical potion': Item('mystical potion', 'Mystical potion to make you invisible'),
    'crystal skull': Item('crystal skull', 'The myth of the crystal skulls is true!'),
    'crystal ball': Item('crystal ball', 'See your future with this crystal ball'),
    'wizzard hat': Item('wizzard hat', 'Channle your inner wizzard with this hat')
}
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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


# # *  Make a new player object that is currently in the 'outside' room.
playerName = input('Please enter your name: ')
player = Player("LDC", room['outside'])


# # *  Write a loop that:
# # * Prints the current room name
# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.
# # *  If the user enters a cardinal direction, attempt to move to the room there.
# # * If the user enters "q", quit the game.
# # *  Print an error message if the movement isn't allowed.

def print_menu():
    print(f"----MENU----")
    print("N: Travel north")
    print("S: Travel south")
    print("E: Travel east")
    print("W: Travel west")
    print("Q: Quit the game")

# # * Prints the current room name


def print_location():
    print(f"---Current Location---\n{player.location.get_name()}")
# # * Prints the current description (the textwrap module might be useful here).
    for line in textwrap.wrap(player.location.get_description()):
        print(f"{line}")


print_menu()
print()
print_location()

while True:
    # # * Waits for user input and decides what to do.
    choice = input("\nWhich way do you want to go?  N, S, E, W or Q to quit: ")

# # *  If the user enters a cardinal direction, attempt to move to the room there.
    if choice == "n":
        if player.location.n_to == None:
            print("Nothing in this direction.")
        else:
            player.location = player.location.n_to
            print(f"---Current Location:---\n{player.location.get_name()}")
            for line in textwrap.wrap(player.location.get_description()):
                print(line)

    elif choice == "e":
        if player.location.e_to == None:
            print("Nothing in this direction.")
        else:
            player.location = player.location.e_to
            print(f"---Current Location:---\n{player.location.get_name()}")
            for line in textwrap.wrap(player.location.get_description()):
                print(line)

    elif choice == "s":
        if player.location.s_to == None:
            print("Nothing in this direction.")
        else:
            player.location = player.location.s_to
            print(f"---Current Location:---\n{player.location.get_name()}")
            for line in textwrap.wrap(player.location.get_description()):
                print(line)

    elif choice == "w":
        if player.location.w_to == None:
            print("Nothing in this direction.")
        else:
            player.location = player.location.w_to
            print(f"---Current Location:---\n{player.location.get_name()}")
            for line in textwrap.wrap(player.location.get_description()):
                print(line)

# # * If the user enters "q", quit the game.
    elif choice == "q":
        print("quit")
        break

  # # *  Print an error message if the movement isn't allowed.
    else:
        print("Invalid direction. Please try again.")
