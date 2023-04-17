import unittest
from src.guests import *
from src.song import *
from src.room import *

# class TestRoom (unittest.TestCase):


    # def setUp(self): 
    #     self.room = Room (1, 3)
    #     self.room.guests= []
    #     # guest1 = Guest ('Wilfred')
    #     # guest2 = Guest ('Mario')

    # def test_room(self):
    #     room = Room(1, 3)
    #     self.assertEqual(room.number, 1)
    #     self.assertEqual(room.capacity, 3)
    #     guest1 = Guest("Wilfred")
    #     guest2 = Guest("Mario")
    #     self.assertTrue(room.add_guest(guest1))
    #     self.assertTrue(room.add_guest(guest2))
    #     guest3 = Guest("Leo")
    #     self.assertTrue(room.add_guest(guest3))
    #     guest4 = Guest("Thierry")
    #     self.assertFalse(room.add_guest(guest4))
    #     self.assertEqual(len(room.guests), 3)




class TestRoom (unittest.TestCase):
    
    def setUp(self):
        self.room = Room(3)

    def test_room(self):
        guest1 = Guest("Wilfred")
        guest2 = Guest("Mario")
        guest3 = Guest("Leo")
        guest4 = Guest("Thierry")
        print("Adding guests to room")
        print(self.room.add_guest(guest1))
        print(self.room.add_guest(guest2))
        print(self.room.add_guest(guest3))
        print(self.room.add_guest(guest4))
        print("Checking room and guest counts")
        print(len(self.room.guests))
        print(len(self.room.next_room.guests))
        print(self.room.next_room.next_room is None)
        self.assertTrue(self.room.add_guest(guest1))
        self.assertTrue(self.room.add_guest(guest2))
        self.assertTrue(self.room.add_guest(guest3))
        self.assertTrue(self.room.next_room is not None)
        self.assertTrue(self.room.next_room.capacity == 3)
        self.assertTrue(self.room.next_room.add_guest(guest4))
        self.assertEqual(len(self.room.guests), 3)
        self.assertEqual(len(self.room.next_room.guests), 3)

