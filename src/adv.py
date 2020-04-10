from room import Room
from player import Player
from item import Item

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

items = {
    'swing': Item('swing', 'a suspended seat for playing or lounging'),
    'mirror': Item('mirror', 'to check yourself out'),
    'table': Item('table', 'furniture piece to set things on'),
    'lamp': Item('lamp', 'something to light the way'),
    'chest': Item('chest', 'something to hold treasure in')
}

room['outside'].add_item(items['swing'])
room['foyer'].add_item(items['mirror'])
room['foyer'].add_item(items['table'])
room['narrow'].add_item(items['lamp'])
room['treasure'].add_item(items['chest'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


player1 = Player('player1', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# print(player1.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
# print(player1.current_room.description)
# * Waits for user input and decides what to do.

# print(input)
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while True:
    command = input(
        'Enter a direction (n, s, e, w) to go different rooms, q to quit, i to see items, g to get items, or d to drop items : ')
    if command == 'n':
        if player1.current_room.n_to != None:
            player1.current_room = player1.current_room.n_to
            print(
                f'room: {player1.current_room.name} \n description: {player1.current_room.description}')
        else:
            print('You cannot move north from this room.')
    elif command == 's':
        if player1.current_room.s_to != None:
            player1.current_room = player1.current_room.s_to
            print(
                f'room: {player1.current_room.name} \n description: {player1.current_room.description}')
        else:
            print('You cannot move south from this room.')
    elif command == 'e':
        if player1.current_room.e_to != None:
            player1.current_room = player1.current_room.e_to
            print(
                f'room: {player1.current_room.name} \n description: {player1.current_room.description}')
        else:
            print('You cannot move east from this room.')
    elif command == 'w':
        if player1.current_room.w_to != None:
            player1.current_room = player1.current_room.w_to
            print(
                f'room: {player1.current_room.name} \n description: {player1.current_room.description}')
        else:
            print('You cannot move west from this room.')
    elif command == 'i':
        if len(player1.current_room.items) > 0:
            for i in player1.current_room.items:
                print(f'name: {i.name} \n description: {i.description}')
    # elif command == 'g':

    elif command == 'q':
        quit()
