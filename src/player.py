# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room  = current_room
        self.items = [] 
    def move_direction(self, direction):
        if getattr(self.current_room, f'{direction}_to') is not None:
            self.current_room = getattr(self.current_room, f'{direction}_to')
            print(self.current_room)
        else:
            print('You have hit a dead end there is no room here', '\n')
    def get_item_string(self):
        if len(self.items) > 0:
            return '\n' + ', '.join([item.name for item in self.items]) + '\n'
    def print_inventory(self):
        print('You are carrying:\n' + ', '.join([item.name for item in self.items]) + '\n')
