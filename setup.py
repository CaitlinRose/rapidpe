# -*- coding: utf-8 -*-

"""RAPID-PE
"""

import os.path
import re
import sys
from glob import glob

from setuptools import (setup, find_packages)


def find_version(path):
    """Parse the __version__ metadata in the given file.
    """
    with open(path, "r") as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# -- dependencies -------------------------------

setup_requires = [
    "setuptools",
]
install_requires = [
    "h5py"
    "lalsuite",
    "lscsoft-glue",
    "matplotlib",
    "numpy",
    "scikit-learn",
    "scipy",
    "six",
]

# run setup
setup(
    # metadata
    name="rapid_pe",
    version=find_version(os.path.join("rapid_pe", "__init__.py")),
    license="FIXME!",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    # content
    packages=find_packages(),
    scripts=list(glob(os.path.join("bin", "rapidpe*"))),
    # dependencies
    setup_requires=setup_requires,
    install_requires=install_requires,
)
