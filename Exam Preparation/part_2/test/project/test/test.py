from project.gallery import Gallery
from unittest import TestCase, main


class GalleryTests(TestCase):
    gallery_name = "TestGallery"
    city = "TestCity"
    area_sq_m = 1.0

    def setUp(self):
        self.gallery = Gallery(self.gallery_name, self.city, self.area_sq_m, True)

    def test_init(self):
        self.assertEqual(self.gallery_name, self.gallery.gallery_name)
        self.assertEqual(self.city, self.gallery.city)
        self.assertEqual(self.area_sq_m, self.gallery.area_sq_m)
        self.assertEqual(True, self.gallery.open_to_public)
        self.assertEqual({}, self.gallery.exhibitions)
        self.assertIsInstance(self.gallery.exhibitions, dict)

    def test_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = ""
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = "AE16!!"
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_invalid_city_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.city = "3Sofia"
        self.assertEqual("City name must start with a letter!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.city = "!!!Sofia"
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_invalid_sq_m_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = 0.0
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = -1.0
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_add_exhibition_name_exists(self):
        self.gallery.exhibitions = {"a": 2000}
        result = self.gallery.add_exhibition("a", 2002)
        expected = 'Exhibition "a" already exists.'
        self.assertEqual(expected, result)
        self.assertEqual(len(self.gallery.exhibitions), 1)

    def test_add_exhibition_name_nonexistent(self):
        self.gallery.exhibitions = {"a": 2000}
        result = self.gallery.add_exhibition("b", 2002)
        expected = 'Exhibition "b" added for the year 2002.'
        self.assertEqual(expected, result)
        self.assertEqual(len(self.gallery.exhibitions), 2)

    def test_remove_exhibition_name_exists(self):
        self.gallery.exhibitions = {"a": 2000}
        result = self.gallery.remove_exhibition("a")
        expected = 'Exhibition "a" removed.'
        self.assertEqual(expected, result)
        self.assertEqual(len(self.gallery.exhibitions), 0)

    def test_remove_exhibition_name_nonexistent(self):
        self.gallery.exhibitions = {"a": 2000}
        result = self.gallery.remove_exhibition("b")
        expected = 'Exhibition "b" not found.'
        self.assertEqual(expected, result)
        self.assertEqual(len(self.gallery.exhibitions), 1)

    def test_list_exhibitions_is_open_to_public(self):
        self.gallery.exhibitions = {"a": 2000, "b": 2002}
        result = self.gallery.list_exhibitions()
        expected = f'a: 2000\nb: 2002'
        self.assertEqual(expected, result)

    def test_list_exhibitions_is_closed_to_public(self):
        self.gallery.exhibitions = {"a": 2000, "b": 2002}
        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        expected = 'Gallery TestGallery is currently closed for public! Check for updates later on.'
        self.assertEqual(expected, result)
        self.assertFalse(self.gallery.open_to_public)

if __name__ == '__main__':
    main()
