class Item:
    def __init__(self, name, description):
        self.item_name = name
        self.item_description = description
    def on_take(self, item):
        print(f'You have picked up {self.item_name}')
    def on_drop(self, item):
        print(f'You have dropped {self.item_name}')
    def can_eat(self):
        return True
    def get_item(self):
        return { 'name': self.item_name, 'description': self.item_description}



