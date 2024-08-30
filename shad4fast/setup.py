from setuptools import find_packages, setup

setup(
    name="shad4fast",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "shad4fast=shad4fast.cli:main",
        ],
    },
)
