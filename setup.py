from setuptools import setup, find_packages

setup(
    name="image_classification",
    version="0.0.1",
    author="Esraa Taha",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)