# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
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
        else:
            return ''
    def print_inventory(self):
        print('You are carrying:\n' + ', '.join([item.item_name for item in self.items]) + '\n')
    
    def getInventory(self, an_item):
        items = []
        for item in self.items:
            fetchedItem = item.get_item()
            items.append(fetchedItem)
        print(f"Here are your items: , {items}")


    def drop_item(self, item):
        for an_item in self.items:
            name = an_item.get_item()['name']
            if name == item:
                self.items.remove(an_item)
                self.current_room.add_item(an_item)
                an_item.on_drop({'name': name})
    def take_items(self, item):
        for an_item in self.items:
            name = an_item.get_item()['name']
            if name == item:
                self.items.append(an_item)
                self.current_room.remove_item(an_item)
                an_item.on_take({'name': name})

    # def take_items(self, it_name):
    #     item_to_take = None
    #     for item in self.items:
    #         if item.item_name.lower() == it_name.lower():
    #             item_to_take = item
    #             break
    #     if item_to_take is None:
    #         print(f'Can not find {it_name} for you to take')
    #         return
    #     if item_to_take.can_take():            
    #         print(f'You took {it_name}')
    #         self.items.remove(item_to_take)
    #     else:
    #         print('You cannot take that!')
    #         return
    # def take_items(self, it_name):
    #     while it_name:
    #         choice = input('Take an item ex. take RedRuby')
    #         choice_arr = choice.split(' ')
    #         if choice_arr[0] == 'take':
    #             for item in it_name:
    #                 item_in_room = item.get_item()
    #                 if item_in_room['name'] == choice_arr[1]:
    #                     self.items.append(item)
    #                     it_name.remove(item)
    #                     self.current_room.updateItems(it_name)
    #                     item.on_take(item_in_room)
    #         elif choice_arr[0] == 'drop':
    #             self.drop_item(choice_arr[1])
    #         else:
    #             print('You did not choose take or drop an item')


