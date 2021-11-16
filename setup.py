from setuptools import find_packages, setup
from fashion-mnist-dataset.project_slug import __version__

setup(
    name="fashion-mnist-dataset.project_slug",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="fashion-mnist-dataset.description",
    author="fashion-mnist-dataset.author",
)
