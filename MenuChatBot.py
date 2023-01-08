from FoodItem import FoodItem


class MenuChatBot:
    appetizers = [
        FoodItem("Fried Mozzarella",
                 "Fried mozzarella cheese with marinara sauce.", 800, 7.99),
        FoodItem(
            "Calamari",
            "Tender calamari, lightly breaded and fried. Served with marinara sauce and spicy ranch.",
            670, 11.79),
        FoodItem(
            "Spinach-Artichoke Dip",
            "A blend of spinach, artichokes and cheeses served warm with flatbread crisps.",
            1160, 10.49),
        FoodItem(
            "Toasted Ravioli",
            "Lightly fried ravioli filled with seasoned beef. Served with marinara sauce.",
            650, 9.29),
        FoodItem("Breadsticks",
                 "Enjoy a freshly-baked, Olive Garden Favorite.", 140, 4.49)
    ]
    entrees = [
        FoodItem(
            "Chicken Alfredo",
            "Creamy alfredo sauce made from scratch with ingredients like parmesan, cream, garlic and butter, served with fettuccine pasta and topped with sliced grilled chicken.",
            1570, 19.29),
        FoodItem(
            "Spaghetti with Meatballs",
            "Spaghetti and meatballs with your choice of marinara or meat sauce. ",
            1120, 16.78),
        FoodItem(
            "Cheese Ravioli",
            "Filled with a blend of indulgent Italian cheeses, topped with your choice of homemade marinara or meat sauce** and melted mozzarella. **Our meat sauce is made with pan-seared beef and Italian sausage.",
            820, 16.49),
        FoodItem(
            "Herb-Grilled Salmon",
            "Filet grilled to perfection and topped with garlic herb butter. Served with parmesan garlic broccoli.",
            490, 20.79),
        FoodItem(
            "6 oz. Sirloin",
            "Grilled 6 oz sirloin topped with garlic herb butter. Served with a side of fettuccine alfredo.",
            890, 18.99)
    ]
    desserts = [
        FoodItem(
            "Strawberry Cream Cake",
            "Vanilla sponge cake layered with sweet vanilla cream and topped with fresh strawberries.",
            540, 9.29),
        FoodItem(
            "Warm Italian Doughnuts",
            "Fried doughnuts tossed in vanilla sugar. Served with raspberry or chocolate sauce.",
            810, 7.99),
        FoodItem(
            "Sicilian Cheesecake with Strawberry Topping",
            "Ricotta cheesecake with a shortbread cookie crust, topped with strawberry sauce.",
            700, 8.79),
    ]

    sides = [
        FoodItem("Side of Meatballs", "Side of meatballs", 480, 3.79),
        FoodItem("Side of Grilled Chicken", "Side of grilled chicken", 130,
                 4.29),
        FoodItem("Side of Broccoli", "Side of broccoli", 35, 2.99),
    ]

    def __init__(self):
        self.bill = 0
        self.foods = {}

    def initiate_chat(self):
        print("Hello, and welcome to the online Olive Garden ordering service.")
        while True:
            print()
            chat_input = input("Would you like to [order], or make a [reservation]? ")
    
            while chat_input.lower() not in ['order', 'reservation']:
                chat_input = input("I don't understand. Could you rephrase it? ")
    
            if chat_input == 'order':
                self.order_menu()
                self.finalize_order()
                return
            elif chat_input == 'reservation':
                self.reservation_menu()
    
    def order_menu(self):
        print()
        print("What would you like to order?")

        while True:
            menu_input = input("""
Categories:
    Appetizers (5 choices)
    Entrées (5 choices)
    Desserts (3 choices)
    Sides (3 choices)
""")
            # Requires valid category to be inputted
            if menu_input == 'done' and self.bill > 0:
                return
            while menu_input.lower() not in ['appetizers', 'entrees', 'desserts', 'sides', 'appetizer', 'entree', 'dessert', 'sides']:
                menu_input = input("Sorry, I don't recognize that category. How about you try something else? ")

            self.view_category(menu_input)
            print()
            self.bill = round(self.bill, 2)
            if self.bill > 0:
                print(f"Your total so far is ${self.bill}.")
                print("If you're done ordering, just say [done].")
                print("Would you like to order anything else?")
            else:
                print("What would you like to order?")

    def view_category(self, category_):
        category = category_
        if category_[-1] != 's':
            category += 's'
        print(f"""
    ———{category.capitalize()}———""")
        for fooditem in getattr(MenuChatBot, category):
            fooditem.print_menu_listing()

        print()
        food_input = input(f"What {category[0:len(category)-1]} would you like? ")

        # Requires valid food to be inputted
        while not self.verify_food(food_input, category):
            food_input = input(f"Sorry, I don't recognize that {category[0:len(category)-1]}. How about you try something else? ")

        self.view_food(self.verify_food(food_input, category, True))
        return

    def view_food(self, fooditem):
        print(f"""
    ———{fooditem.name}———""")
        print(f"    ${fooditem.price}")
        fooditem.print_description()
        print()
        order_input = input("Would you like to order this? ")

        # requires valid response
        while order_input.lower() not in ['yes', 'no']:
            order_input = input("I don't understand. Could you rephrase it? ")

        if order_input.lower() in ['yes']:
            self.bill += fooditem.price
            if fooditem.name not in self.foods:
                self.foods[fooditem.name] = 1
            else:
                self.foods[fooditem.name] += 1
        elif order_input in ['no']:
            return

    # check if inputted food exists
    def verify_food(self, food, category, return_food=False):
        for fooditem in getattr(MenuChatBot, category):
            if fooditem.name.lower() == food.lower():
                if return_food:
                    return fooditem
                else:
                    return True
        return False

    def finalize_order(self):
        print()
        for food in self.foods:
            if self.foods[food] > 1:
                print(f"    {food} (x{self.foods[food]})")
            else:
                print(f"    {food}")
        print()
        print(f"Your total is ${self.bill}. Thanks for ordering!")

    def reservation_menu(self):
        print()
        day_input = input("What day will the reservation be on? ")
        while day_input.lower() not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            day_input = input("Sorry, I don't understand. We only allow reservations on any day during the week. ")

        time_input = input("What time will the reservation be at? ")

        while True:
            try:
                time_input = int(time_input)
                break
            except:
                time_input = input("Sorry, I don't understand. Could you rephrase? ")

        while int(time_input) <= 0 or int(time_input) > 24:
            time_input = input("Sorry, I don't understand. Could you rephrase? ")
            try:
                time_input = int(time_input)
                break
            except:
                continue

        print(f"Your reservation has been set for {time_input} on {day_input}.")