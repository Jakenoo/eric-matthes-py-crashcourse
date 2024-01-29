import restauraunt
class IceCreamStand(restauraunt.Restauraunt):
    """Restauraunt subclass for ice cream type cuisine"""
    def __init__(self, restauraunt_name, cuisine_type):
        super().__init__(restauraunt_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry', 'mint', 'coffee']
    
    # two methods for changing default flavor list and displaying said list
    def update_flavors(self, flavor_selection):
        self.flavors = flavor_selection
    def show_flavors(self):
        print(f"Here are the available flavors in {self.restauraunt_name}:")
        for flavor in self.flavors:
            print(f"\t{flavor}")

iceys = IceCreamStand("Icey's", "Ice Cream")
iceys.show_flavors()
iceys.update_flavors(['matcha', 'ube', 'honey-vanilla'])
iceys.show_flavors()