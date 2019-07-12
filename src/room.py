# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []
    def __str__(self):
        str = f'''
            \n----
            \n{self.name}
            \n  {self.description}\n
            \n{self._get_exits_string()}\n
            \n {self._get_item_string()}'''
        return str

    def _get_item_string(self):
        if len(self.items) > 0:
            return '\n' + ', '.join([item.item_name for item in self.items]) + '\n'
        else:
            return ''

    def _get_exits_string(self):
        exits = []
        if self.n_to is not None:
            exits.append('n')
        if self.s_to is not None:
            exits.append('s')
        if self.e_to is not None:
            exits.append('e')
        if self.w_to is not None:
            exits.append('w')
        return 'Exits:' + ', '.join(exits)
    def add_item(self, item_name):
        self.items.append(item_name)
    def remove_item(self, item_name):
        self.items.remove(item_name)
    def check_for_items(self):
        if self.items:
            print('You are carrying:\n' + ', '.join([item.item_name for item in self.items]) + '\n')
        else:
            print('There are no items')
            return None
    def updateItems(self, newItems):
        self.items = newItems
    pass



