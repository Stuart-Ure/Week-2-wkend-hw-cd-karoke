import unittest
from src.guests import Guest
from src.song import Song
from src.room import Room

class TestSong (unittest.TestCase):
    def setUp(self):
        self.song = Song("Blank Space", "Taylor Swift")
        self.song2 = Song("Pineapple", "Caamp")
        self.song3 = Song("Dont You Want Me ", "Human League")
        self.song4 = Song("Nose Bleed Section", "Hilltop Hoods")
    
    def test_song(self):
        self.assertEqual(self.song.title, "Blank Space")
        self.assertEqual(self.song.artist, "Taylor Swift")