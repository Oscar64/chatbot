class FoodItem:
    listing_length = 60
    description_width = 75
    tab_length = 4
    
    def __init__(self, name, description, calories, price):
        self.name = name
        self.description = description
        self.calories = calories
        self.price = price

    def print_menu_listing(self):
        print(f"{self.name.ljust((FoodItem.listing_length-4)-len(str(self.price)), '.')}${self.price}")

    def print_description(self):
        description_words = self.description.split(' ')
        line = ""

        for word in description_words:
            if len(line+word) > FoodItem.description_width-FoodItem.tab_length:
                print(" "*FoodItem.tab_length+line)
                line = ""
            line += word + " "
        if len(line) > 0:
            print(" "*FoodItem.tab_length+line)

        print(f"{' '*FoodItem.tab_length}{self.calories} cal.")