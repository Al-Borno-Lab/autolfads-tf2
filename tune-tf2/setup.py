from setuptools import find_packages, setup

setup(
    name="tune_tf2",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ray[tune]",
    ],
    author="Andrew Sedler",
    author_email="arsedler9@gmail.com",
    description="Hyperparameter utilities for LFADS",
)
