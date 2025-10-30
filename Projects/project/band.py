from project.album import Album
from project.song import Song

class Band:
    def __init__(self, name:str):
        self.name = name
        self.albums = []

    def add_album(self, album:Album):
        if album in self.albums:
           return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name:str):
        a = next((a for a in self.albums if a.name == album_name), None)
        if a and a.published:
            return "Album has been published. It cannot be removed."
        if a:
            self.albums.remove(a)
            return f"Album {a.name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = '\n'.join(al.details for al in self.albums)
        return f"Band {self.name}\n{result}\n"


band = Band("Death")
album = Album("The Sound of Perseverance")
print(band.remove_album("The Sound of Perseverance"))
expected = "Album The Sound of Perseverance is not found."

# band = Band("Death")
# album = Album("The Sound of Perseverance")
# print(album.publish())
# print(band.add_album(album))
# print(band.remove_album("The Sound of Perseverance"))
# expected = "Album has been published. It cannot be removed."


# band = Band("Death")
# album = Album("The Sound of Perseverance")
# print(album.publish())
# print(band.add_album(album))
# print(band.remove_album("The Sound of Perseverance"))
# expected = "Album has been published. It cannot be removed."



