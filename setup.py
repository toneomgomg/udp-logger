# Copyright (C) 2019 Thomas Hellström <rel@xed.se>
#
# This file is part of ez-gecos.
#
# ez-gecos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ez-gecos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ez-gecos.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="udp-logger",
    version='0.0.1',
    description="Simple UDP logger.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tone Hellström, Henrik Pira",
    author_email="tone.hellstrom@inter.ikea.com, henrik.pira@inter.ikea.com",
    #url="https://github.com/",
    #license='GPLv3',
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    # classifiers=[
    #     #   3 - Alpha
    #     #   4 - Beta
    #     #   5 - Production/Stable
    #     'Development Status :: 4 - Beta',

    #     # Audience
    #     'Intended Audience :: Developers',

    #     # License
    #     'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

    #     # Python versions (Only tested on Python 3.7)
    #     'Programming Language :: Python :: 3.7',

    #     # Operating system (Only tested on Linux)
    #     'Operating System :: POSIX :: Linux',

    #     # Topic
    #     'Topic :: Software Development :: Libraries :: Python Modules'
    # ],
)
