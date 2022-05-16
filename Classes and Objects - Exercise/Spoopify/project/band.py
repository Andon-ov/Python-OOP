from project.album import Album


# class Band:
#     def __init__(self, name):
#         self.name = name
#         self.albums = []
#
#     def add_album(self, new_album: Album):
#         for album in self.albums:
#             if album.name == new_album:
#                 return f"Band {self.name} already has {new_album} in their library."
#
#         self.albums.append(new_album)
#         return f"Band {self.name} has added their newest album {new_album.name}."
#
#     def remove_album(self, album_name: str):
#
#         for album in self.albums:
#             if album.name == album_name:
#                 if album.published:
#                     return "Album has been published. It cannot be removed."
#                 else:
#                     self.albums.remove(album_name)
#                     return f"Album {album_name} has been removed."
#
#         return f"Album {album_name} is not found."
#
#     def details(self):
#         data = f"Band {self.name}\n"
#         for album in self.albums:
#             data += album.details()
#         return data

from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):

        for album in self.albums:
            if album.name == album_name and album.published is True:
                return "Album has been published. It cannot be removed."

            if album.name == album_name:
                self.albums.remove(album)
                return f"Album {album_name} has been removed."

            return f"Album {album_name} is not found."

    def details(self):
        data = f"Band {self.name}\n"
        for album in self.albums:
            data += album.details()
        return data