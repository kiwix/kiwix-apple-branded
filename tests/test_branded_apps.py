import unittest
from branded_apps import BrandedApps
from pathlib import Path


class BrandedAppsTest(unittest.TestCase):

    def setUp(self):
        self.branded = BrandedApps(brands=["dwds"], build_number=1)

    def test_branded_plist(self):
        self.branded.create_plists(
            branded_plist=Path("tests")/"Support"/"Info.plist")

    def test_branded_project_creation(self):
        self.branded.create_branded_project_file(
            path=Path()/"branded_project_test.yml")

    def x_test_downloads(self):
        self.branded.download_zim_files()

    def x_test_download_commands(self):
        for cmd in self.branded._curl_download_commands():
            print(cmd)
