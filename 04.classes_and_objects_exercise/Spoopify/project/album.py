from project.song import Song
#
#
# class Album:
#     def __init__(self, name, *songs):
#         self.songs = [x for x in songs]
#         self.published = False
#         self.name = name
#
#     def add_song(self, new_song: Song):
#         if new_song.single:
#             return f"Cannot add {new_song.name}. It's a single"
#
#         if self.published:
#             return "Cannot add songs. Album is published."
#
#         for song in self.songs:
#             if new_song.name == song.name:
#                 return "Song is already in the album."
#
#         self.songs.append(new_song)
#         return f"Song {new_song.name} has been added to the album {self.name}."
#
#     def remove_song(self, song_name: str):
#         if self.published:
#             return "Cannot remove songs. Album is published."
#         for song in self.songs:
#
#             if song_name == song.name:
#                 self.songs.remove(song_name)
#                 return f"Removed song {song_name} from album {self.name}."
#
#         return "Song is not in the album."
#
#     def details(self):
#         data = f"Album {self.name}" + "\n"
#         for song in self.songs:
#             data += f"== {song.get_info()}\n"
#         return data
#
#     def publish(self):
#         if self.published:
#             return f"Album {self.name} is already published."
#
#         self.published = True
#         return f"Album {self.name} has been published."

class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = [x for x in songs]

    def add_song(self, second_song:Song):
        if self.published is True:
            return "Cannot add songs. Album is published."

        if second_song in self.songs:
            return "Song is already in the album."

        if second_song.single is True:
            return f"Cannot add {second_song.name}. It's a single"

        self.songs.append(second_song)
        return f"Song {second_song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published is True:
            return "Cannot remove songs. Album is published."

        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published is True:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        data = f"Album {self.name}"
        for song in self.songs:
            data += "\n"
            data += f"== {song.get_info()}"
        data += "\n"
        return data