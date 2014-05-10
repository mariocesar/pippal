# encoding: utf8
from __future__ import unicode_literals

"""
Pippal, Copyright (C) 2014  Mario César Señoranis Ayala

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

from optparse import OptionParser

usage = "usage: %prog"

class Command:
    parser = OptionParser(
        usage=usage,
        version='%prog 0.1.dev1',
        description="With Pippal manage your python packages easily and with style.",
        epilog=("Contribute to this project, report bugs, ask for features "
                "and get the latest features visiting: "
                "https://github.com/mariocesar/pippa.")
    )

    def run(self):
        (options, args) = self.parser.parse_args()
