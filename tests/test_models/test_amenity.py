#!/usr/bin/python3
"""

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """ Below are tests for the Amenity class """

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amenity_ = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amenity_.__dict__)

    def test_two_amenities_unique_ids(self):
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        self.assertNotEqual(amenity_1.id, amenity_2.id)

    def test_two_amenities_different_created_at(self):
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertLess(amenity_1.created_at, amenity_2.created_at)

    def test_two_amenities_different_updated_at(self):
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertLess(amenity_1.updated_at, amenity_2.updated_at)

    def test_str_representation(self):
        date_time = datetime.today()
        date_time_repr = repr(dt)
        amenity_ = Amenity()
        amenity_.id = "123456"
        amenity_.created_at = amenity_.updated_at = date_time
        amenity_str = amenity_.__str__()
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'created_at': " + date_time_repr, amenity_str)
        self.assertIn("'updated_at': " + date_time_repr, amenity_str)

    def test_args_unused(self):
        amenity_ = Amenity(None)
        self.assertNotIn(None, amenity_.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """ Below are tests for kwargs() """
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        amenity_ = Amenity(id="345", created_at = date_time_iso, updated_at = date_time_iso)
        self.assertEqual(amenity_.id, "345")
        self.assertEqual(amenity_.created_at, date_time)
        self.assertEqual(amenity_.updated_at, date_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """ Tests for the Amenity class """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        amenity_ = Amenity()
        sleep(0.05)
        first_updated_at = amenity_.updated_at
        amenity_.save()
        self.assertLess(first_updated_at, amenity_.updated_at)

    def test_two_saves(self):
        amenity_ = Amenity()
        sleep(0.05)
        first_updated_at = amenity_.updated_at
        amenity_.save()
        second_updated_at = amenity_.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenity_.save()
        self.assertLess(second_updated_at, amenity_.updated_at)

    def test_save_with_arg(self):
        amenity_ = Amenity()
        with self.assertRaises(TypeError):
            amenity_.save(None)

    def test_save_updates_file(self):
        amenity_ = Amenity()
        amenity_.save()
        amenity_id = "Amenity." + amenity_.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """ Tests to_dict() in the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amenity_ = Amenity()
        self.assertIn("id", amenity_.to_dict())
        self.assertIn("created_at", amenity_.to_dict())
        self.assertIn("updated_at", amenity_.to_dict())
        self.assertIn("__class__", amenity_.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amenity_ = Amenity()
        amenity_.middle_name = "Holberton"
        amenity_.my_number = 98
        self.assertEqual("Holberton", amenity_.middle_name)
        self.assertIn("my_number", amenity_.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amenity_ = Amenity()
        amenity_dict = amenity_.to_dict()
        self.assertEqual(str, type(amenity_dict["id"]))
        self.assertEqual(str, type(amenity_dict["created_at"]))
        self.assertEqual(str, type(amenity_dict["updated_at"]))

    def test_to_dict_output(self):
        date_time = datetime.today()
        amenity_ = Amenity()
        amenity_.id = "123456"
        amenity_.created_at = amenity_.updated_at = date_time
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(amenity_.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        amenity_ = Amenity()
        self.assertNotEqual(amenity_.to_dict(), amenity_.__dict__)

    def test_to_dict_with_arg(self):
        amenity_ = Amenity()
        with self.assertRaises(TypeError):
            amenity_.to_dict(None)


if __name__ == "__main__":
    unittest.main()
