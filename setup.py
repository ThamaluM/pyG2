import setuptools
from pathlib import Path

setuptools.setup(

    name = "pyG2",
    version = "0.0alpha",
    long_description = Path("README.md").read_text(),
    packages = setuptools.find_packages(exclude=['test'])

)