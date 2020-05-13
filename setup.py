import setuptools
from pathlib import Path

setuptools.setup(

    name = "pyG2",
    version = "0.0alpha",
    author = "Thamalu Maliththa Piyadigama",
    long_description = Path("README.md").read_text(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/ThamaluM/pyG2",
    packages = setuptools.find_packages(exclude=['test','.git'])

)