import unittest
from src.guests import *
from src.song import *
from src.room import *

    
class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Wilfred")
        self.song1 = Song("Blank Space", "Taylor Swift")
        self.song2 = Song("Pineapple", "Caamp")
        self.song3 = Song("Dont You Want Me ", "Human League")
        self.song4 = Song("Nose Bleed Section", "Hilltop Hoods")
    
    def test_guest(self):
        self.assertEqual(self.guest.name, "Wilfred")
        
        # add multiple songs to guest's song list
        self.guest.songs = [self.song1, self.song2, self.song3, self.song4]
        
        # check that the songs are added to the guest's song list
        self.assertEqual(len(self.guest.songs), 4)
        self.assertEqual(self.guest.songs[0].title, "Blank Space")
        self.assertEqual(self.guest.songs[3].artist, "Hilltop Hoods")
        
        # let the guest sing one of the songs
        song_to_sing = self.guest.songs[1]
        self.assertEqual(self.guest.sing(song_to_sing), "Wilfred is singing Pineapple by Caamp")
