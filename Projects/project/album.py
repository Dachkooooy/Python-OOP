from project.song import Song


class Album:
    def __init__(self, name:str, *singles):
        self.name = name
        self.singles = singles
        self.published = False
        self.songs: list[Song] = []

    def add_song(self, song: Song):
        if self.singles:
            for s in self.singles:
                self.songs.append(s)
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        s = next((s for s in self.songs if s.name == song_name), None)
        if self.published:
            return "Cannot remove songs. Album is published."
        elif not s:
            return "Song is not in the album."
        self.songs.remove(s)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."


    def details(self):
        if self.songs:
           result = "\n".join(s.get_info() for s in self.songs)
           return f"Album {self.name}\n== {result}\n"
        else:
           return f"Album {self.name}\n"








