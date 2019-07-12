from room import Room
from player import Player
from item import *

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

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Previous day's non-DRY code 
# player1 = Player('player1', room['outside'])
# # print(f'\n Player Name: {player1.name} \n Room name: {player1.current_room.name}, \n Room desc: {player1.current_room.description}')
# # x = getattr(player1.current_room, 'name')
# # x = hasattr(player1.current_room, 'name')
# # print(x)

# while True:
#     direction_moves = ['n', 's', 'w', 'e', 'q']
#     direction_input = input('Type n, s, w, e to move to a another room and q to quit game ')
#     # print(f'Hello {player1.name}, You are now in {player1.current_room.name} that is {player1.current_room.description}')
#     try:

#         if direction_input in direction_moves:
#             if hasattr(player1.current_room, 'name') is False:
#                 print('Sorry this is a dead end pick another location')
#                 break
#             # elif direction_input == 'n' or 's':
#             else:
#                 if direction_input == 'n':
#                     player1.current_room = player1.current_room.n_to
#                     print(f'{player1.current_room.name}, {player1.current_room.description}')
#                 if direction_input == 's':
#                     player1.current_room = player1.current_room.s_to
#                     print(f'{player1.current_room.name}, {player1.current_room.description}')
#                 if direction_input == 'w':
#                     player1.current_room = player1.current_room.w_to
#                     print(f'{player1.current_room.name}, {player1.current_room.description}')
#                 if direction_input == 'e':
#                     player1.current_room = player1.current_room.e_to
#                     print(f'{player1.current_room.name}, {player1.current_room.description}')

#                 elif direction_input == 'q':
#                     print('Goodbye!')
#                     break
#         else:
#             print('Not a valid direction move, choose n, s, w, e, or q to quit')
#     except AttributeError:
#         print('Sorry this is a dead end pick another location')


player1 = Player('player1', room['outside'])

ruby = Item('RedRuby', 'This is red ruby.')
gem = Item('Green Gem', 'This is green gem')
redbull = Item('RedBull', 'Red bull energy power')

room['outside'].items.append(ruby)
room['outside'].items.append(gem)
player1.items.append(redbull)

current_room = player1.current_room

print(current_room)

valid_directions = ['n', 's', 'e', 'w']

while True:
    cmd = input('Type n, s, w, e to move to a another room, q to quit game, i to print inventory,  ')
    if cmd in valid_directions:
        player1.move_direction(cmd)
    elif cmd == 'i':
        player1.print_inventory()
    elif cmd == 'q':
        print('Goodbye!')
        exit()
    elif cmd.startswith('drop'):
        player1.drop_item(cmd.split(' ')[1])
    # elif cmd.startswith('take'):
    #     player1.getInventory(cmd.split(' ')[1])
    elif cmd.startswith('take'):
        player1.take_items(cmd.split(' ')[1])
   