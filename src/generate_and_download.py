#!/usr/bin/env python3

"""Generate the branded app plist files, and a branded_project.yml. 
Based on the arguments passed in:  
where the subfolder name will become the "brand name" of the branded app.
"""

from branded_apps import BrandedApps
from pathlib import Path


def main():
    brand = Path(".brand_name").read_text()
    build_number = int(Path(".build_number").read_text())

    branded_apps = BrandedApps(brands=[brand], build_number=build_number)
    # create the plist files
    branded_apps.create_plists(branded_plist=Path("Branded.plist"))

    # download the zim files
    branded_apps.download_zim_files()

    # finally create the project file, containing all brands as targets
    branded_apps.create_branded_project_file(path=Path("branded_project.yml"))


if __name__ == "__main__":
    main()
