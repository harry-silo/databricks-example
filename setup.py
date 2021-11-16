from setuptools import find_packages, setup

setup(
    name="fashion-mnist-dataset.project_slug",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=1,
    description="fashion-mnist-dataset.description",
    author="fashion-mnist-dataset.author",
)
