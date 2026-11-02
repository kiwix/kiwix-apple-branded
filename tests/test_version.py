import unittest
from version import Version


class VersionTest(unittest.TestCase):

    def test_version_from_filename(self):
        version = Version.from_file_name(
            "dwds_de_dictionary_nopic_2023-11-20", build_number=10)
        self.assertEqual(version.semantic, "2023.11.10")

        version = Version.from_file_name(
            "dwds_de_dictionary_nopic_2023-09-20", build_number=0)
        self.assertEqual(version.semantic, "2023.9.0")

        version = Version.from_file_name(
            "dwds_de_dictionary_nopic_2023-01", build_number=7)
        self.assertEqual(version.semantic, "2023.1.7")

        version = Version.from_file_name(
            "dwds_de_dictionary_nopic_2023-12", build_number=129)
        self.assertEqual(version.semantic, "2023.12.129")

    def test_version_from_filename_with_suffix(self):
        version = Version.from_file_name(
            "phet_mul_all_2026-02a", build_number=0)
        self.assertEqual(version.semantic, "2026.2.0")
        self.assertEqual(version.suffix, "a")
        self.assertEqual(version.date_token, "2026.02a")

        version = Version.from_file_name(
            "phet_mul_all_2026-02ab", build_number=3)
        self.assertEqual(version.semantic, "2026.2.3")
        self.assertEqual(version.suffix, "ab")
        self.assertEqual(version.date_token, "2026.02ab")

    def test_version_without_suffix_has_empty_suffix(self):
        version = Version.from_file_name(
            "phet_mul_all_2026-02", build_number=0)
        self.assertEqual(version.suffix, "")
        self.assertEqual(version.date_token, "2026.02")

    def test_version_equality_includes_suffix(self):
        self.assertEqual(
            Version(2026, 2, 0, suffix="a"),
            Version.from_file_name("phet_mul_all_2026-02a", build_number=0))
        self.assertNotEqual(
            Version(2026, 2, 0, suffix="a"),
            Version.from_file_name("phet_mul_all_2026-02", build_number=0))
        self.assertNotEqual(
            Version(2026, 2, 0, suffix="a"),
            Version(2026, 2, 0, suffix="b"))
