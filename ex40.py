class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def something_else(self):
        print("Do something else")

happy_bday_lyrics = ["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right there"] 

happy_bday = Song(happy_bday_lyrics)

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

another_song = Song(["This is another song ..."])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

another_song.sing_me_a_song()

another_song.something_else()