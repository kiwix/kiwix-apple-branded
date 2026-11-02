#!/usr/bin/env python3

import re
from datetime import datetime


class Version:

    def __init__(self, year: int, month: int, build_number: int, suffix: str = ""):
        if (1 <= month <= 12) == False:
            raise ValueError(f"invalid month: {month}")
        if (0 <= build_number) == False:
            raise ValueError(f"invalid build number: {build_number}")
        max_year = datetime.now().year + 5
        if (2000 < year < max_year) == False:
            raise ValueError(f"invalid year: {year}")
        if re.fullmatch(r"[a-z]{0,2}", suffix) is None:
            raise ValueError(f"invalid suffix: {suffix}")

        self.year = year
        self.month = month
        self.build_number = build_number
        self.suffix = suffix
        self.semantic = f"{year}.{month}.{build_number}"

    @classmethod
    def from_file_name(self, file_name: str, build_number: int):
        p = re.compile(
            '(?P<year>\\d{4})-(?P<month>\\d{1,2})(?P<suffix>[a-z]{0,2})')
        m = p.search(file_name)
        return Version(year=int(m.group('year')),
                       month=int(m.group('month')),
                       build_number=build_number,
                       suffix=m.group('suffix'))

    @property
    def date_token(self) -> str:
        """Content date as used in tags: YYYY.MM[suffix]."""
        return f"{self.year}.{self.month:02d}{self.suffix}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Version):
            return (self.semantic == other.semantic
                    and self.suffix == other.suffix)
        return False
