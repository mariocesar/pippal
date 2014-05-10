# encoding: utf8
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

from __future__ import unicode_literals

# Initial setup based on github.com/pypa/pip/blob/develop/setup.py
import codecs
import os
import re
import sys

from babel.messages import frontend as babel
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    # https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):

    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


long_description = open('README.rst', 'r').read()

package_name = "pippal"

setup(
    name=package_name,
    version=find_version(package_name, "__init__.py"),
    description="Manage your python packages easily and with style.",
    long_description=long_description,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development :: Build Tools"
    ],
    keywords='virtualenv setuptools pip',
    author='Mario César Señoranis Ayala',
    author_email='mariocesar@creat1va.com',
    url='https://github.com/mariocesar/{0}'.format(package_name),
    license='GPL2',
    packages=find_packages(exclude=["docs", "tests*"]),
    include_package_data=True,
    install_requires=(),
    entry_points={
        "console_scripts": [
            "{0}={0}:main".format(package_name),
        ],
    },
    cmdclass = {
        'compile_catalog': babel.compile_catalog,
        'extract_messages': babel.extract_messages,
        'init_catalog': babel.init_catalog,
        'update_catalog': babel.update_catalog
    },
    zip_safe=False
)