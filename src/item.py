class Item:
    def __init__(self, name, description):
        self.item_name = name
        self.item_description = description
    def on_take(self):
        print(f'You have picked up {self.item_name}')
    def on_drop(self):
        print(f'You have dropped {self.item_name}')

