import setuptools
from pathlib import Path

setuptools.setup(

    name = "pyG2",
    version = "1.0beta1",
    author = "Thamalu Maliththa Piyadigama",
    description = "Grammar of graphics for python",
    long_description = Path("README.md").read_text(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/ThamaluM/pyG2",
    packages = setuptools.find_packages(exclude=['test','.git','examples','docs']),
    install_requires=["ipython", "pandas"],
    package_data = {"":["*.js"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python ",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)