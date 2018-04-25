class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
lyrics1 = ["Happy bday to you",
            "I don't want to get sued",
            "So I'll stop right there"]
lyrics2 = ["They rally around the family",
            "With pockets full of shells"]

happy_bday = Song(lyrics1)
bulls_on_parade = Song(lyrics2)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
