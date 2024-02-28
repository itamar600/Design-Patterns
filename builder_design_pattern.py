class Burger:
    def __init__(self):
        self.buns = None  # Initialize buns attribute
        self.patty = None  # Initialize patty attribute
        self.dress = None  # Initialize dress attribute

    def setBuns(self, bunStyle):  # Method to set the type of bun
        self.buns = bunStyle
    
    def setPatty(self, pattyStyle):  # Method to set the type of patty
        self.patty = pattyStyle
    
    def setDress(self, dressStyle):  # Method to set the type of dressing
        self.dress = dressStyle

    def print_burger(self):  # Method to print the burger's components
        print(f"Burger\n Buns: {self.buns}, Patty: {self.patty}, Dress: {self.dress}")


class BurgerBuilder:
    def __init__(self) -> None:
        self.burger = Burger()  # Initialize a Burger object

    def addBuns(self, bunStyle):  # Method to add buns to the burger
        self.burger.setBuns(bunStyle)  # Set the buns style
        return self
    
    def addPatty(self, pattyStyle):  # Method to add a patty to the burger
        self.burger.setPatty(pattyStyle)  # Set the patty style
        return self
    
    def addDress(self, dressStyle):  # Method to add dressing to the burger
        self.burger.setDress(dressStyle)  # Set the dressing style
        return self
    
    def build(self):  # Method to build the burger
        return self.burger  # Return the constructed burger

# Creating a burger using the builder pattern
burger = BurgerBuilder() \
            .addBuns("sesame") \
            .addPatty("soy-patty") \
            .addDress("1000-islands") \
            .build()  # Build the burger

burger.print_burger()  # Print the details of the constructed burger
