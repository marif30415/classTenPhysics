import setuptools
from pathlib import Path
setuptools.setup(
    name = "classTenPhysics",
    version = 1.0,
    long_discription =Path("README.md").read_text(),
    packages = setuptools.find_packages(exclude=['tests'])

)