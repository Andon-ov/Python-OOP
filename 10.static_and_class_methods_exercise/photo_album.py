








































# from math import ceil
#
#
# class PhotoAlbum:
#     PHOTOS_PER_PAGE = 4
#
#     def __init__(self, pages):
#         self.pages = pages
#         self.photos = self.__build_photos()
#
#     def add_photo(self, label):
#         for row_idx, row in enumerate(self.photos):
#             if len(row) < 4:
#                 self.photos[row_idx].append(label)
#                 return f"{label} photo added successfully on page {row_idx + 1} slot {len(self.photos[row_idx])}"
#         return "No more free slots"
#
#     def display(self):
#         separator = "-" * 11
#         result = separator + "\n"
#         for row in self.photos:
#             result += " ".join(["[]" for x in row])+"\n"
#             result += separator + "\n"
#
#         return result.strip()
#
#     @classmethod
#     def from_photos_count(cls, photos_count: int):
#         pages = ceil(photos_count // cls.PHOTOS_PER_PAGE)
#         return cls(pages)
#
#     def __build_photos(self):
#         result = []
#         for i in range(self.pages):
#             result.append([])
#         return result
#
#
# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())
