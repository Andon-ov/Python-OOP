from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.build_photos()

    def build_photos(self):
        result = []
        for _ in range(self.pages):
            result.append([] * self.PHOTOS_PER_PAGE)
        return result

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        #  have a error here with //
        return cls(pages)


    def add_photo(self, label: str):
        for idx, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[idx].append(label)
                return f"{label} photo added successfully on page {idx + 1} slot {len(self.photos[idx])}"
                # page.append(label)
                # return f"{label} photo added successfully on page {idx + 1} slot {len(page)}"

        return "No more free slots"

    def display(self):
        sep = "-" * 11
        result = sep + '\n'
        for row in self.photos:
            result += ' '.join(['[]' for _ in row]) + '\n'
            result += sep + '\n'

        return result.strip()


# album = PhotoAlbum(2)

# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())

import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free slots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")


if __name__ == "__main__":
    unittest.main()
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
