# class Room:
    
#     def __init__(self, room_number, capacity):
#         self.number = room_number
#         self.capacity = capacity
#         self.guests = []

class Room:
    
    room_count = 0
    
    def __init__(self, capacity):
        Room.room_count += 1
        self.number = Room.room_count
        self.capacity = capacity
        self.guests = []
        self.next_room = None
        self.songs = []  # list of available songs delete if doesnt work

    def add_song(self, song):
        self.songs.append(song)

    def add_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
            return True
        elif self.next_room is not None:
            return self.next_room.add_guest(guest)
        else:
            self.next_room = Room(self.capacity)
            return self.next_room.add_guest(guest)
        
    def print_guests_and_songs(self):
        for guest in self.guests:
            for song in self.songs:
                print(guest.sing(song))