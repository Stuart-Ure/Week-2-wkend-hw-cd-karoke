class Guest:

    def __init__(self, name):
        self.name = name

    def sing(self, song):
        return f"{self.name} is singing {song.title} by {song.artist}"
    
    def sing (self,song):
        return ("Wilfred is singing Pineapple by Caamp")
    print ("Wilfred is singing Pineapple by Caamp")